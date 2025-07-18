// client/src/App.js
import React, { useState } from 'react';
import { Container, Typography } from '@mui/material';
import FileUpload from './components/FileUpload';
import PromptInput from './components/PromptInput';
import DownloadZipButton from './components/DownloadZipButton';
import Notebook from './components/Notebook';

function App() {
  const [sessionId, setSessionId] = useState('');
  const [headers, setHeaders] = useState([]);
  const [steps, setSteps] = useState([]);

  // Called when dataset is uploaded
  const handleUploadSuccess = ({ sessionId, columns }) => {
    setSessionId(sessionId);
    setHeaders(columns);
    setSteps([]); // reset notebook steps
  };

  // Called when user submits a prompt
  const handlePromptSubmit = async (prompt) => {
    if (!sessionId || headers.length === 0) return;

    try {
      const response = await fetch('http://localhost:5000/generate-code', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt, headers, sessionId }),
      });

      const data = await response.json();

      if (data.code) {
        const stepNum = data.step;

        // Try loading text output
        const textOutput = await fetch(`http://localhost:5000/sessions/${sessionId}/output_step_${stepNum}.txt`)
          .then(res => (res.ok ? res.text() : null))
          .catch(() => null);

        // Try loading image output
        const imageUrl = `http://localhost:5000/sessions/${sessionId}/output_step_${stepNum}.png`;
        const imageExists = await fetch(imageUrl)
          .then(res => res.ok)
          .catch(() => false);

        const output = imageExists
          ? { type: 'image', content: imageUrl }
          : textOutput
          ? { type: 'text', content: textOutput }
          : null;

        // Add step to notebook
        setSteps(prev => [
          ...prev,
          {
            prompt,
            code: data.code,
            output,
          },
        ]);
      }
    } catch (error) {
      console.error('Error generating code:', error);
    }
  };

  return (
    <Container sx={{ mt: 5 }}>
      <Typography variant="h4" gutterBottom>🧠 Prompt2LLM Notebook</Typography>

      <FileUpload onSuccess={handleUploadSuccess} />

      {sessionId && (
        <>
          <PromptInput onSubmit={handlePromptSubmit} />
          <DownloadZipButton sessionId={sessionId} />
          <Notebook steps={steps} />
        </>
      )}
    </Container>
  );
}

export default App;
