import React, { useRef, useEffect } from 'react';
import { useLocation, Switch } from 'react-router-dom';
import AppRoute from './utils/AppRoute';
import ScrollReveal from './utils/ScrollReveal';
import ReactGA from 'react-ga';


// Layouts
import LayoutDefault from './layouts/LayoutDefault';

// Views 
import Home from './views/Home';
import Fire from './views/Fire'
import Hurricane from './views/Hurricane'; 
import Flood from './views/Flood'; 
import Info from "./views/info"
import info from './views/info';

// Initialize Google Analytics
ReactGA.initialize(process.env.REACT_APP_GA_CODE);

const trackPage = page => {
  ReactGA.set({ page });
  ReactGA.pageview(page);
};

const App = () => {

  const childRef = useRef();
  let location = useLocation();

  useEffect(() => {
    const page = location.pathname;
    document.body.classList.add('is-loaded')
    childRef.current.init();
    trackPage(page);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [location]);

  return (
    <ScrollReveal
      ref={childRef}
      children={() => (
        <Switch>
          <AppRoute exact path="/" component={Home} layout={LayoutDefault} />
          <AppRoute exact path="/fire" component={Fire} layout={LayoutDefault}/>
          <AppRoute exact path="/hurricane" component={Hurricane} layout={LayoutDefault}/>
          <AppRoute exact path="/flood" component={Flood} layout={LayoutDefault}/>
          <AppRoute exact path="/info" component={info} layout={LayoutDefault}/>
        </Switch>
      )} />
  );
}

export default App;