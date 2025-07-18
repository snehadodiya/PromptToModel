import React, { useState } from 'react';
import { Button, Box, Typography } from '@mui/material';
import axios from 'axios';

const FileUpload = ({ onSuccess }) => {
  const [file, setFile] = useState(null);
  const [fileName, setFileName] = useState('');
  const [response, setResponse] = useState('');

  const handleChange = (e) => {
    const selectedFile = e.target.files[0];
    if (selectedFile) {
      setFile(selectedFile);
      setFileName(selectedFile.name);
    }
  };

  const handleUpload = async () => {
    if (!file) {
      setResponse('Please select a file first.');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
      const res = await axios.post('http://localhost:5000/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      if (res.data?.columns && onSuccess) {
        onSuccess(res.data); // returns { sessionId, columns }
        setResponse('File uploaded successfully!');
      } else {
        setResponse('Upload failed: No headers found.');
      }
    } catch (err) {
      console.error(err);
      setResponse('Upload failed: ' + (err.response?.data?.message || err.message));
    }
  };

  return (
    <Box sx={{ p: 3 }}>
      <Typography variant="h6">Upload CSV/XLS file</Typography>
      <input type="file" accept=".csv,.xlsx" onChange={handleChange} />
      {fileName && (
        <Typography variant="body1" sx={{ mt: 1 }}>
          Selected file: {fileName}
        </Typography>
      )}
      <Button
        variant="contained"
        color="primary"
        onClick={handleUpload}
        disabled={!file}
        sx={{ mt: 2 }}
      >
        Upload
      </Button>
      {response && (
        <Typography sx={{ mt: 2, color: response.includes('failed') ? 'error.main' : 'success.main' }}>
          {response}
        </Typography>
      )}
    </Box>
  );
};

export default FileUpload;
