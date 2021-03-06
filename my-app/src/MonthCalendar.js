import React, { Component } from 'react';
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";

class MonthCalendar extends Component {
  state = {
    startDate: ''
  };
 
  handleChange = date => {
    this.setState({
      startDate: date
    });
  };
 
  render() {
    return (
      <DatePicker
        selected={this.state.startDate}
        onChange={this.handleChange}
		dateFormat="MM/yyyy"
		showMonthYearPicker
      />
    );
  }
}

export default MonthCalendar;