import React from "react";
import SignUpLogIn from "./components/SignUpLogIn";
import LandingPage from "./components/LandingPage";
import Profile from "./components/Profile";
import { BrowserRouter, Route, Link, Switch } from "react-router-dom";
import PostFeedPage from "./components/NewsFeed";
import "./App.css";

const App = () => {
  return (
    <>
      <BrowserRouter>
        <Switch>
          <Route exact path="/" component={LandingPage} />
          <Route exact path="/Gateway" component={SignUpLogIn} />
          <Route exact path="/Profile/:req_Profile" component={Profile} />
          <Route exact path="/NewsFeed" component={PostFeedPage} />
        </Switch>
      </BrowserRouter>
    </>
  );
};

export default App;
