import './App.css';
import PatientRow from './components/PatientRow';
import { Component } from 'react';
import Triage from './components/triage_dropdown';
import './components/styles.css';

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
        <PatientRow key={index} pName={patient.name} number={patient.number} timestamp={patient.timestamp} linkToReport={'Click to View Report'} patientID={patient.id} urgency={< Triage key={index + 'triage'} />} />
      );
    })

    return (
      <div className="App">
        <div className="MainContainer">
          <h1 className="header-container">Patient Data</h1>
          <table className="table-container">
            <thead>
              <tr>
                <th>Name</th>
                <th>Number</th>
                <th>Timestamp</th>
                <th></th>
                <th>Prediction</th>
                <th>Urgency</th>
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
