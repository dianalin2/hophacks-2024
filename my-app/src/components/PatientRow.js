import React, { Component } from 'react';
import './styles.css';

class PatientRow extends Component {
    constructor() {
        super();
        this.startCall = this.startCall.bind(this);
    }

    startCall() {
        fetch(`/api/patientpdf/${this.props.patientID}/startcall`)
            .then(response => response.json())
            .then(data => {
                console.log(data);
            })
            .catch(error => {
                console.error(error);
            });
    }

    render() {
        console.log(this.pName)
        return (
            <tr className='trBody'>
                <td className='td'>{this.props.pName}</td>
                <td className='td'>{this.props.number}</td>
                <td className='td'>{this.props.timestamp}</td>
                <td className='td'><button onClick={this.startCall}>Start Pre-Call</button></td>
                <td className='td'><a href={`/api/patientpdf/${this.props.patientID}`} target="_blank" rel="noreferrer">{this.props.linkToReport}</a></td>
                <td className='td'>{this.props.urgency}</td>
            </tr>
        );
    }
}

export default PatientRow;
