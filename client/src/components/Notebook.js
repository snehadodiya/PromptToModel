// client/src/components/Notebook.js
import React from 'react';
import { Paper, Typography, Box } from '@mui/material';

const Notebook = ({ steps }) => {
  return (
    <Box sx={{ mt: 4 }}>
      {steps.map((step, index) => (
        <Paper key={index} sx={{ p: 2, mb: 3, backgroundColor: '#f9f9f9' }}>
          <Typography variant="subtitle1">📝 Step {index + 1}</Typography>
          <Typography variant="body2" sx={{ fontStyle: 'italic' }}>
            Prompt: {step.prompt}
          </Typography>
          <Typography variant="subtitle2" sx={{ mt: 1 }}>Generated Code:</Typography>
          <pre style={{ background: '#eee', padding: '10px' }}>{step.code}</pre>

          {step.output && step.output.type === 'text' && (
            <>
              <Typography variant="subtitle2" sx={{ mt: 1 }}>Output:</Typography>
              <pre style={{ background: '#e0f7fa', padding: '10px' }}>{step.output.content}</pre>
            </>
          )}

          {step.output && step.output.type === 'image' && (
            <>
              <Typography variant="subtitle2" sx={{ mt: 1 }}>Visualization:</Typography>
              <img
                src={step.output.content}
                alt="Step Output"
                style={{ maxWidth: '100%', marginTop: '10px' }}
              />
            </>
          )}
        </Paper>
      ))}
    </Box>
  );
};

export default Notebook;
