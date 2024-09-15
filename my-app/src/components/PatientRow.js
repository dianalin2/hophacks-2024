import React, { useState } from 'react';
import pdf from "./document.pdf";

function PatientRow ({ patientID, name, number, timestamp, linkToReport}) {
    return ( 
        <tr>
            <td>{name}</td>
            <td>{number}</td>
            <td>{timestamp}</td>
            <td><a href={pdf} target="_blank" rel="noreferrer">{linkToReport}</a></td>
        </tr>
    );
};

export default PatientRow;