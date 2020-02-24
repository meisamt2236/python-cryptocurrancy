import React, {useState, useEffect} from 'react';
import logo from '../assets/logo.svg';
import '../App.css';

function App() {
  const [walletInfo, setWalletInfo]= useState({});
  useEffect(() => {
    fetch('http://localhost:5000/wallet/info').then(response => response.json()).then(json => setWalletInfo(json));
  }, []);
  const {address, balance} = walletInfo;
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Welcome to the Pychain world!
        </p>
        <div>
          <div className="WalletInfo">
            Address: {address}
          </div>
          <div className="WalletInfo">
            Balance: {balance}
          </div>
        </div>
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
