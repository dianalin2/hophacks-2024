import './App.css';
import Triage from './components/triage_dropdown';
import PDFviewer from './components/pdfviewer';
import PatientRow from './components/PatientRow';

function App() {
  return (
    <div className="App">
      {/* <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <Triage />

      </header>
      </header>
      <PDFviewer/> */}
      <div className="MainContainer">
        <p className="AppTitle">Patient Data</p>
        <table className="InfoTable">
          <thead>
            <tr>
              <th>Name</th>
              <th>Number</th>
              <th>Timestamp</th>
              <th>Prediction</th>
            </tr>
          </thead>
          <tbody>
            <PatientRow patientID={123} name="Andrew Hong" number="217-281-1471" timestamp="9/14/24 9:38pm" linkToReport="Click me!"/>
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default App;
