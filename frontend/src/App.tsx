import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import ClientSummary from './components/ClientSummary';
import OrderLog from './components/OrderLog';
import ErrorReport from './components/ErrorReport';

const App: React.FC = () => {
  return (
    <Router>
      <div className="app">
        <h1 className="text-center text-2xl font-bold">Stock Order Punching System</h1>
        <Switch>
          <Route path="/" exact component={ClientSummary} />
          <Route path="/order-log" component={OrderLog} />
          <Route path="/error-report" component={ErrorReport} />
        </Switch>
      </div>
    </Router>
  );
};

export default App;