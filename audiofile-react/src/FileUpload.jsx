import { useState } from "react";
import ReactAudioPlayer from "react-audio-player";
import "./FileUpload.css";

function AudioUploader() {
  const [selectedFiles, setSelectedFiles] = useState([]);
  const [uploadStatus, setUploadStatus] = useState([]);
  const [metaData, setMetaData] = useState([]);
  const [fetchStatus, setFetchStatus] = useState("empty");

  const handleFileChange = (event) => {
    const newFiles = Array.from(event.target.files);
    console.log(newFiles);
    setSelectedFiles((prevFiles) => [...newFiles, ...prevFiles]);
    for (var i = 0; i < Object.keys(newFiles).length; i++) {
      setUploadStatus((prevStatus) => ["notUploaded", ...prevStatus]);
    }
  };

  const fetchAudioData = async () => {
    setFetchStatus("loading");
    fetch("http://localhost:8000/fileupload/", {
      method: "GET",
    })
      .then((response) => response.json())
      .then((data) => {
        for (const element of data) {
          const data_obj = {
            name: element.file_name,
            type: element.file_type,
            size: element.file_size,
            location: element.file_location,
          };
          // const updatedStatus = [...uploadStatus];
          // updatedStatus[index] = "success";
          setFetchStatus("success")
          setUploadStatus((prevStatus) => [...prevStatus, "success"]);
          setMetaData((prevMetaData) => [...prevMetaData, data_obj]);
          setSelectedFiles((prevFiles) => [...prevFiles, data_obj]);
        }

        console.log(data);
      })
      .catch(console.error);
  };

  const fetchFromDB = async (location) => {
    location = location.slice(2);
    console.log(`http://localhost:8000/fileupload${location}`);

    const link = document.createElement("a");
    link.href = `http://localhost:8000/fileupload${location}`;
    // link.target = "_blank";  // Open in a new tab

    // Programmatically trigger a click on the <a> element
    link.click();

    // fetch(`http://localhost:8000/fileupload${location}`, {
    //   method: "GET",
    // })
    // .then((response) => {console.log(response)})
    // .catch(console.error)
  };

  const handleUpload = async (file, index) => {
    const updatedStatus = [...uploadStatus];
    updatedStatus[index] = "uploading";
    setUploadStatus(updatedStatus);

    const formData = new FormData();
    formData.append("form_file", file);

    fetch("http://localhost:8000/fileupload/", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        data = data[0];
        const updatedStatus = [...uploadStatus];
        updatedStatus[index] = "success";
        setUploadStatus(updatedStatus);
        console.log(data.file_location);
        const updatedMetaData = [...metaData];
        const data_obj = {
          name: data.file_name,
          type: data.file_type,
          size: data.file_size,
          location: data.file_location,
        };
        updatedMetaData[index] = data_obj;
        setMetaData(updatedMetaData);
      })
      .catch((error) => {
        const updatedStatus = [...uploadStatus];
        updatedStatus[index] = "error";
        setUploadStatus(updatedStatus);
        console.log(error);
      });
  };

  return (
    <div className="audio-uploader">
      <h2>Audio Uploader and Player</h2>
      <input
        type="file"
        accept="audio/*"
        name="file"
        multiple
        onChange={handleFileChange}
      />
      <br />
      <button onClick={fetchAudioData}> Sync with the database</button>
      <br/>
      {fetchStatus==="loading" && <span className="loader"></span>}
      {selectedFiles.length > 0 && (
        <table className="file-table">
          <thead>
            <tr>
              <th>File Name</th>
              <th>Play</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            {selectedFiles.map((file, index) => (
              <tr key={index}>
                <td>{file.name}</td>
                <td>
                  {file.type.startsWith("audio/") ? (
                    <ReactAudioPlayer
                      src={URL.createObjectURL(file)}
                      controls
                    />
                  ) : (
                    <>
                      <button onClick={() => fetchFromDB(file.location)}>
                        Download from DB
                      </button>
                      {/* <div>{file.location}</div> */}
                    </>
                  )}
                </td>
                <td>
                  {uploadStatus[index] === "uploading" && (
                    <span className="loader"></span>
                  )}
                  {uploadStatus[index] === "notUploaded" && (
                    <button onClick={() => handleUpload(file, index)}>
                      Upload
                    </button>
                  )}
                  {uploadStatus[index] === "success" && (
                    <>
                      <p className="green-text">File submitted !</p>
                      {metaData[index] && (
                        <div className="meta_data">{`File Type: ${metaData[index].type}`}</div>
                      )}
                      {metaData[index]  && (
                        <div className="meta_data">{`File Type: ${metaData[index].size}`}</div>
                      )}                      
                    </>
                  )}
                  {uploadStatus[index] === "error" && (
                    <p>File upload failed.</p>
                  )}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default AudioUploader;
