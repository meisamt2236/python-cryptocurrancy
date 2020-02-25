import React, {useState, useEffect} from 'react';
import logo from '../assets/logo.svg';
import '../App.css';
import Blockchain from './Blockchain';
import {API_BASE_URL} from '../config';

function App() {
  const [walletInfo, setWalletInfo]= useState({});
  useEffect(() => {
    fetch(`${API_BASE_URL}/wallet/info`).then(response => response.json()).then(json => setWalletInfo(json));
  }, []);
  const {address, balance} = walletInfo;
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h3>
          Welcome to the Pychain world!
        </h3>
        <div>
          <div>
            Address: {address}
          </div>
          <div>
            Balance: {balance}
          </div>
        </div>
        <Blockchain/>
        <a
          className="App-link"
          href="https://github.com/meisamt2236/python-blockchain"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn more
        </a>
      </header>
    </div>
  );
}

export default App;
