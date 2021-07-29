import React, { useState, useEffect } from 'react';
import axios from 'axios';

const App = () => {
  const [response, setResponse] = useState('');

  const callApi = () => {
    axios.get(`http://localhost:8000`)
      .then(res => {
        console.log(res)
        setResponse(res.data)
      })
      .catch((err) => {
        console.log(err);
      });
    setResponse('qqqqq')
  }

  return (
    <React.Fragment>
      <div>{response}</div>
      <button onClick={callApi}>call api</button>
    </React.Fragment>
  );
}



export default App;
