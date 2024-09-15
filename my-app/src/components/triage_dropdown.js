import React from 'react';

const MyForm = () => {
  // Define the styles for each option
  const optionStyles = {
    emergency: {
      backgroundColor: '#ff3131',
      color: 'white',
      fontFamily: "'Trebuchet MS', sans-serif",
      padding: '10px'
    },
    veryUrgent: {
      backgroundColor: '#f8a41d',
      color: 'white',
      fontFamily: "'Trebuchet MS', sans-serif",
      padding: '10px'
    },
    urgent: {
      backgroundColor: '#fccd08',
      color: 'white',
      fontFamily: "'Trebuchet MS', sans-serif",
      padding: '10px'
    },
    routine: {
      backgroundColor: '#18b38e',
      color: 'white',
      fontFamily: "'Trebuchet MS', sans-serif",
      padding: '10px'
    }
  };

  return (
    <form action="/action_page.php">
      <select name="Triage" id="Triage">
        <option value="Emergency" style={optionStyles.emergency}>
          Emergency
        </option>
        <option value="Very Urgent" style={optionStyles.veryUrgent}>
          Very Urgent
        </option>
        <option value="Urgent" style={optionStyles.urgent}>
          Urgent
        </option>
        <option value="Routine" style={optionStyles.routine}>
          Routine
        </option>
      </select>
    </form>
  );
};

export default MyForm;
