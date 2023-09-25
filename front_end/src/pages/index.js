
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Index() {
//   const [greeting, setGreeting] = useState("");

  const [inputData, setInputData] = useState("");
    const [result, setResult] = useState(null);

    const sendDataToBackend = () => {
        axios.post('http://localhost:5000/api/mainCOPY', {
            input: inputData
        })
        .then(response => {
            setResult(response.data.message);
        })
        .catch(error => {
            console.error("There was an error sending data to the backend!", error);
        });
    };


//   useEffect(() => {
//     axios.get('http://localhost:5000/api/greeting')
//       .then(response => {
//         setGreeting(response.data.message);
//       })
//       .catch(error => {
//         console.error("There was an error fetching the greeting!", error);
//       });
//   }, []);

  return (
    <div>
      {/* {greeting} */}
      
        <input
            type="text"
            value={inputData}
            onChange={e => setInputData(e.target.value)}
        />
        <button onClick={sendDataToBackend}>Send to Backend</button>
        {result && (
  <div>
    {Object.entries(result).map(([timeStamp, value], index) => (
      <p key={index}>
        {timeStamp}: {value}
      </p>
    ))}
  </div>
)}

        
    </div>
  );
}

export default Index;
