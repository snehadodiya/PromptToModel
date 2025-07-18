const express = require('express');
const multer = require('multer');
const cors = require('cors');
const { spawn } = require('child_process');
const path = require('path');
const fs = require('fs');
const archiver = require('archiver');

const app = express();
app.use(cors());
app.use(express.json());

// Setup file upload and session paths
const upload = multer({ dest: 'uploads/' });
const sessionsRoot = path.join(__dirname, '..', 'sessions');
app.use('/sessions', express.static(sessionsRoot));

// ✅ File Upload Endpoint
app.post('/upload', upload.single('file'), (req, res) => {
  const { originalname, path: tempPath } = req.file;
  const sessionId = req.body.sessionId || `session_${Date.now()}`;
  const sessionDir = path.join(sessionsRoot, sessionId);
  if (!fs.existsSync(sessionDir)) fs.mkdirSync(sessionDir, { recursive: true });

  const destPath = path.join(sessionDir, 'dataset.csv');
  fs.renameSync(tempPath, destPath);

  const csv = fs.readFileSync(destPath, 'utf-8');
  const headers = csv.split('\n')[0].split(',');

  res.json({ message: 'Upload successful', columns: headers, sessionId });
});

// ✅ Code Generation Route
app.post('/generate-code', (req, res) => {
  const { prompt, headers, sessionId } = req.body;
  console.log("➡️ Received generate-code request:", { prompt, headers, sessionId });

  if (!prompt || !headers || !sessionId) {
    return res.status(400).json({ error: 'Missing fields' });
  }

  const sessionDir = path.join(sessionsRoot, sessionId);
  if (!fs.existsSync(sessionDir)) fs.mkdirSync(sessionDir);

  const files = fs.readdirSync(sessionDir);
  const stepCount = files.filter(f => f.startsWith('step_')).length + 1;
const python = spawn('python', [
  path.join(__dirname, 'python', 'llm_engine.py'),
  prompt,
  JSON.stringify(headers),
], {
  cwd: sessionDir, // ✅ This makes dataset.csv available to the Python script
});

  let output = '', errorOutput = '';
  python.stdout.on('data', data => output += data.toString());
  python.stderr.on('data', data => errorOutput += data.toString());

  python.on('close', code => {
    const slug = prompt.toLowerCase().split(' ').slice(0, 3).join('_').replace(/[^a-z_]/g, '');
    const filename = `step_${stepCount}_${slug}.py`;
    const filepath = path.join(sessionDir, filename);

    if (code === 0) {
      const preamble = 'import pandas as pd\nimport matplotlib.pyplot as plt\n\ndf = pd.read_csv("dataset.csv")\n\n';
      const finalCode = preamble + output;
      fs.writeFileSync(filepath, finalCode);

      // Check if output was written (text or image)
      const txtPath = path.join(sessionDir, `output_step_${stepCount}.txt`);
      const pngPath = path.join(sessionDir, `output_step_${stepCount}.png`);

      let responsePayload = {
        code: finalCode,
        filename,
        step: stepCount
      };

      if (fs.existsSync(txtPath)) {
        responsePayload.outputPreviewUrl = `/sessions/${sessionId}/output_step_${stepCount}.txt`;
      } else if (fs.existsSync(pngPath)) {
        responsePayload.plotUrl = `/sessions/${sessionId}/output_step_${stepCount}.png`;
      }

      return res.json(responsePayload);
    } else {
      console.error("❌ Python script failed:\n", errorOutput);
      return res.status(500).json({
        error: 'Script execution failed',
        code,
        stderr: errorOutput,
        filename: `step_${stepCount}_${slug}.py`,
        codeOutput: output
      });
    }
  });
});

// ✅ ZIP Download Route
app.get('/download/:sessionId', (req, res) => {
  const sessionId = req.params.sessionId;
  const sessionDir = path.join(sessionsRoot, sessionId);
  if (!fs.existsSync(sessionDir)) return res.status(404).send('Session not found');

  // Write README.md
  const readme = `# ML Pipeline - ${sessionId}

## How to Run

\`\`\`bash
pip install -r requirements.txt
python pipeline.py
\`\`\`

## Files Included
- dataset.csv (your uploaded dataset)
- pipeline.py (runs all steps sequentially)
- step_X.py files (individual ML steps)
- output_step_X.png or .txt (intermediate visualizations)
`;
  fs.writeFileSync(path.join(sessionDir, 'README.md'), readme);

  // Create pipeline.py by chaining step files
  const stepFiles = fs.readdirSync(sessionDir)
    .filter(f => f.startsWith('step_') && f.endsWith('.py'))
    .sort();

  const pipelineCode = [
    "import pandas as pd",
    "import matplotlib.pyplot as plt",
    "df = pd.read_csv('dataset.csv')",
    ...stepFiles.map(f => `\n# ---- ${f} ----\n` + fs.readFileSync(path.join(sessionDir, f), 'utf-8'))
  ].join('\n\n');
  fs.writeFileSync(path.join(sessionDir, 'pipeline.py'), pipelineCode);

  // Write requirements.txt
  const requirements = ['pandas', 'scikit-learn', 'matplotlib'].join('\n');
  fs.writeFileSync(path.join(sessionDir, 'requirements.txt'), requirements);

  // Create ZIP
  const zipName = `${sessionId}.zip`;
  res.setHeader('Content-Disposition', `attachment; filename=${zipName}`);
  res.setHeader('Content-Type', 'application/zip');

  const archive = archiver('zip', { zlib: { level: 9 } });
  archive.pipe(res);
  archive.directory(sessionDir, false);
  archive.finalize();
});

// ✅ Start Server
app.listen(5000, () => console.log('✅ Server running on http://localhost:5000'));
