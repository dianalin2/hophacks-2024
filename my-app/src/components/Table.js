import React from "react";
// import Triage from './triage_dropdown';
// import PDFviewer from './pdfviewer';
// import PatientRow from './PatientRow';
import "./styles.css";

const Table = ({ data }) => {
  const keys = Object.keys(data[0]);
  return (
    <p>
      <table className="table">
        <thead className="thead">
          <tr className="trHead">
            {keys.map((item, index) => (
              <th className="th" key={index}>{item}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {data.map((obj, index) => (
            <tr className="trBody" key={index}>
              {keys.map((item, index) => {
                const value = obj[item];
                return (
                  <td className="td" key={index}>{value}</td>
                );
              })}
            </tr>
          ))}
        </tbody>
      </table>
    </p>
  );
};






// function Table() {
//   return (
//     <div className="Table">
//       <div className="MainContainer">
//         <h1 className="AppTitle">Patient Data</h1>
//         <table className="InfoTable">
//           <thead>
//             <tr>
//               <th>Name</th>
//               <th>Number</th>
//               <th>Timestamp</th>
//               <th>Prediction</th>
//             </tr>
//           </thead>
//           <tbody>
//             <PatientRow patientID={123} name="Andrew Hong" number="217-281-1471" timestamp="9/14/24 9:38pm" linkToReport="Click me!"/>
//           </tbody>
//         </table>
//       </div>
//     </div>
//   );
// }

export default Table;
