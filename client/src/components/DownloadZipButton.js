import React from 'react';
import { Button, Box, Typography } from '@mui/material';

const DownloadZipButton = ({ sessionId }) => {
  const downloadZip = async () => {
    try {
      const res = await fetch(`http://localhost:5000/download/${sessionId}`);
      if (!res.ok) throw new Error('Failed to download ZIP');

      const blob = await res.blob();
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `${sessionId}.zip`;
      a.click();
      window.URL.revokeObjectURL(url);
    } catch (err) {
      console.error('❌ Download failed:', err);
      alert('Download failed. Check if the session ZIP is ready.');
    }
  };

  return (
    
    <Button
        variant="contained"
        color="primary"
        onClick={downloadZip}
        disabled={!sessionId}
        sx={{ mt: 2 }}
      >
      📦 Download ZIP
    </Button>
  );
};

export default DownloadZipButton;
