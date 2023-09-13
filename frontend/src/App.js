import logo from './logo.svg';
import './App.css';

const apiUrl = process.env.REACT_APP_API_URL;

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        {/* Input to be squared */}
        <input type="number" id="number" name="number" />
        {/* Button that sends an API request to current URL, and displays the output */}
        <button onClick={async () => {
          const number = document.getElementById("number").value;
          const response = await fetch(`${apiUrl}/api/square/${number}`);
          const data = await response.json();
          alert(data.message);
        }}>Square (send API request to backend)</button>

      </header>
    </div>
  );
}

export default App;
