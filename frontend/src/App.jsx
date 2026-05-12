import { useState } from "react";
import axios from "axios";

function App(){
  const [file, setFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    setFile(selectedFile);
    setResult(null);

    if (selectedFile){
      setPreview(URL.createObjectURL(selectedFile));
    }
  };

  const handlePredict = async () => {
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    try{
      setLoading(true);
      const response = await axios.post(
        "http://127.0.0.1:8000/predict",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );
      setResult(response.data);
    } catch (error) {
      console.error("prediction error:", error);
      alert("Prediction failed!");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{
      maxWidth: "700px",
      margin: "40px auto",
      padding: "20px",
      textAlign: "center",
      fontFamily: "Arial, sans-serif",
    }}>
      <h1>CIFAR-10 Image Classification</h1>
      <input type="file" accept="image/*" onChange={handleFileChange}/> 
      {preview && (
        <div style={{marginTop: "20px"}}>
          <img src={preview} alt="Preview" style={{
            width: "300px",
            maxWidth: "100%",
            borderRadius: "10px",
          }}/>
        </div>
      )}

      <div style={{marginTop: "20px"}}>
        <button onClick={handlePredict}
        disabled={!file || loading}
        style={{
          padding: "10px 20px",
          fontSize: "16px",
          cursor: "pointer"
        }}>{loading ? "Predicting...": "Predict"}</button>
      </div>

      {result && (
        <div style={{
          marginTop: "30px",
          padding: "20px",
          border: "1px solid #ddd",
          borderRadius: "10px"
        }}>
          <h2>Prediction Result</h2>
          <p>
            <strong>Class:</strong>{result.predicted_class}
          </p>
          <p>
            <strong>Confidence:</strong>{" "}{(result.confidence * 100).toFixed(2)}%
          </p>
        </div>
      )}

    </div>
  );
}

export default App;