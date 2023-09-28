import React, { useState, useEffect } from 'react';
import axios from 'axios';
import YouTubeEmbed from '../components/youTubeEmbed';

import Button from '@mui/material/Button';


function Index() {
//   const [greeting, setGreeting] = useState("");

  const [inputData, setInputData] = useState("");
  const [result, setResult] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

    const sendDataToBackend = () => {
        setIsLoading(true);
        axios.post('http://localhost:5000/api/mainCOPY', {
            input: inputData
        })
        .then(response => {
            setResult(response.data.message);
        })
        .catch(error => {
            console.error("There was an error sending data to the backend!", error);
        })
        .finally(() => {
          setIsLoading(false);
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
        <Button variant="contained" onClick={sendDataToBackend}>Send to Backend</Button>
        {isLoading ? (<div><p>HELLO!</p></div>) : (
          result && (
            <div>
              {Object.entries(result).map(([timeStamp, value], index) => (
                <YouTubeEmbed url={value} />


                // <p key={index}>
                //   {timeStamp}: {value}
                // </p>
              ))}
            </div>
          )
        )
          
        
        }

        
    </div>
  );
}

export default Index;
