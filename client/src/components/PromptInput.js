import React, { useState } from 'react';
import { Box, TextField, Button, Typography } from '@mui/material';

const PromptInput = ({ onSubmit }) => {
  const [prompt, setPrompt] = useState('');
  const [sessionId] = useState('session_1234'); // Static session ID for now

  const handleSubmit = () => {
    if (prompt.trim()) {
      onSubmit(prompt, sessionId); // Pass both prompt and sessionId to parent
      setPrompt('');
    }
  };

  return (
    <Box sx={{ mt: 4 }}>
      <Typography variant="h6" gutterBottom>
        Describe your ML task
      </Typography>
      <TextField
        fullWidth
        multiline
        minRows={3}
        placeholder="e.g. Build a classification model to predict churn"
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            handleSubmit(); // ✅ Now safely defined above
          }
        }}
      />
      <Button
        variant="contained"
        color="secondary"
        sx={{ mt: 2 }}
        onClick={handleSubmit}
        disabled={!prompt.trim()}
      >
        Generate ML Code
      </Button>
    </Box>
  );
};

export default PromptInput;
