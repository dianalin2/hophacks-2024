import './App.css';
import Triage from './components/triage_dropdown';
import PDFviewer from './components/pdfviewer';
import PatientRow from './components/PatientRow';
import { Component } from 'react';

class App extends Component {
  constructor() {
    super();
    this.state = {
      data: []
    }
  }

  async componentDidMount() {
    const res = await fetch(`/api/userdata`);

    const data = await res.json();

    console.log(data);

    this.setState({
      data: data
    });
  }

  render() {
    const patientRows = this.state.data.map((patient, index) => {
      return (
        <PatientRow key={index} pName={patient.name} number={patient.number} timestamp={patient.timestamp} linkToReport={'Click to View Report'} patientID={patient.id} />
      );
    })

    return (
      <div className="App">
        <div className="MainContainer">
          <p className="AppTitle">Patient Data</p>
          <table className="InfoTable">
            <thead>
              <tr>
                <th>Name</th>
                <th>Number</th>
                <th>Timestamp</th>
                <th></th>
                <th>Prediction</th>
              </tr>
            </thead>
            <tbody>
              {patientRows}
            </tbody>
          </table>
        </div>
      </div>
    );
  }
}

export default App;
