import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Link, Switch } from 'react-router-dom';
import DemandeDevis from 'components/DemandeDevis';
import AOS from 'aos';
import Sticky from 'sticky-js';
import { isMobile } from 'react-device-detect';
import DetailsFormation from 'components/DetailsFormation';
import DemandePartenariat from 'components/DemandePartenariat';
import DetailsClubs from 'components/DetailsClubs/clubsdetails';
import DF from 'components/DF';

import 'aos/dist/aos.css';
import './fonts.css';

class App extends Component {
  componentDidMount() {
    setTimeout(() => {
      AOS.init({
        offset: isMobile ? 10 : 100,
      });

      this.stickey = new Sticky('.sticky-effect');
    }, 1500);
  }

  componentDidUpdate() {
    AOS.refresh();
    if (this.stickey) {
      this.stickey.destory();
      this.stickey = new Sticky('.sticky-effect');
    }
  }

  render() {
    return (
      <Router hashType="noslash" basename={process.env.BASE_PATH}>
        <Switch>
          <Route exact path="/">
            <div>
              Pages: <br />
              <Link to="/DemandeDevis">DemandeDevis     </Link>
              <Link to="/DetailsFormation">DetailsFormation</Link>
              <Link to="/DemandePartenariat">DemandePartenariat</Link>
              <Link to="/ClubsDetails">DetailsClubs</Link>
              <Link to="/DF">                               DF</Link>
            </div>
          </Route>

          <Route exact path="/DemandeDevis" component={DemandeDevis} />
          <Route exact path="/DetailsFormation" component={DetailsFormation} />
          <Route exact path="/DemandePartenariat" component={DemandePartenariat} />
          <Route exact path="/DF" component={DF} />
          <Route exact path="/ClubsDetails" component={DetailsClubs} />
        </Switch>
      </Router>
    );
  }
}

export default App;
