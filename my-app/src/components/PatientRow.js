import React, { Component } from 'react';

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
            <tr>
                <td>{this.props.pName}</td>
                <td>{this.props.number}</td>
                <td>{this.props.timestamp}</td>
                <td><button onClick={this.startCall}>Start Pre-Call</button></td>
                <td><a href={`/api/patientpdf/${this.props.patientID}`} target="_blank" rel="noreferrer">{this.props.linkToReport}</a></td>
            </tr>
        );
    }
}

export default PatientRow;
