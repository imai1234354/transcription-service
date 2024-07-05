import React, { useState } from 'react';
import { Storage, API } from 'aws-amplify';

function App() {
  const [file, setFile] = useState(null);
  const [transcription, setTranscription] = useState('');

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    setFile(file);
  };

  const handleUpload = async () => {
    if (file) {
      const filename = file.name;
      await Storage.put(filename, file);
      alert('File uploaded successfully');

      const apiName = 'transcriptionAPI';
      const path = '/transcribe';
      const response = await API.post(apiName, path, {
        body: { key: filename },
      });
      alert(response);
    }
  };

  return (
    <div className="App">
      <h1>Transcription Service</h1>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>
      <div>
        <h2>Transcription</h2>
        <p>{transcription}</p>
      </div>
    </div>
  );
}

export default App;
