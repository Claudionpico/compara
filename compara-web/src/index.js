import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import reportWebVitals from './reportWebVitals';
import FormCar from './components/form/formCar'
import 'bootstrap/dist/css/bootstrap.min.css';

ReactDOM.render(
  <React.StrictMode>
    <FormCar />
  </React.StrictMode>,
  document.getElementById('root')
);

reportWebVitals();
