import React, { useState } from "react";
import { useHistory } from "react-router-dom";
import axios from "axios";
import "./CSS/SignUpLogIn/SignUpLogIn.css";

const SignUpLogIn = () => {
  const [LogInStat , setLogInStat] = useState(true)
  const [SignUpStat , setSignUpStat] = useState("default")
  const [addclass, setaddclass] = useState("");
  const [SignUpInfo, setSignUpInfo] = useState({
    Username: "",
    Firstname:"",
    Lastname:"",
    Gender:"",
    Email: "",
    Password: "",
  });

  const [Creds, setCreds] = useState({
    Username: "",
    Password: "",
  });

  let history = useHistory();

  const handleSignUp = (event) => {
    event.preventDefault();

    if (event.target.name === "")
    {
      const data = {
        Username: SignUpInfo.Username,
        Firstname : SignUpInfo.Firstname,
        Lastname : SignUpInfo.Lastname,
        Gender : SignUpInfo.Gender,
        Email: SignUpInfo.Email,
        Password: SignUpInfo.Password,
      };
      
      
      axios(
        {
          method:'post',
          url:'http://127.0.0.1:8000/SignUp/',
          data:data 
        }
      ).then(
        ((response)=>
        {
          
          if(response.data.msg==="Please try with different Username")
          { 
            setSignUpStat("Use Diff Username")
          }
          else if(response.data.msg=== 'Please try with different Email')
            setSignUpStat("Use Diff Email")
          
          else
            setSignUpStat("Ok")
        }),
        ((error)=>{console.log(error)})
      )
    } 
    
    else {
      setSignUpInfo({
        ...SignUpInfo,
        [event.target.name]: event.target.value,
      });
    }
  };

  const handleLogIn = (event) => {
    event.preventDefault();

    if (event.target.name === "") {
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/LogIn/",
        data: {
          Username: Creds.Username,
          Password: Creds.Password,
        },
      }).then(
        (response) => {
          if(response.data.msg === 'Please LogIn with correct credentials')
            setLogInStat(false)
          else
          {
            axios({
            method: "post",
            url: "http://127.0.0.1:8000/getToken/",
            data: {
              username: Creds.Username,
              password: Creds.Password,
            },
          }).then(
            (response) => {
              
              const access_token = response.data.access;
              const refresh_token = response.data.refresh;
              localStorage.setItem("access_token", access_token);
              localStorage.setItem("refresh_token", refresh_token);
              localStorage.setItem("profile_name", Creds.Username);
              console.log("Redirecting....");
              const url = "/NewsFeed";
              history.push(url);
              
            },
            (error) => {
              console.log(error);
            }
          );
        }
        },
        (error) => {
          console.log(error);
        }
      );

    } else {

      setCreds({
        ...Creds,
        [event.target.name]: event.target.value,
      });
    }
  };

  return (
    <div className="login-body">
      <div className={`container ${addclass}`} id="container">
        <div className="form-container  sign-up-container">
          <form className="login-form" onSubmit={handleSignUp}>
            <h1>Create Account</h1>
            <input
              className="login-input"
              type="text"
              placeholder="USERNAME"
              name="Username"
              value={SignUpInfo.Username}
              onChange={handleSignUp}
            />

            <input
              className="login-input"
              type="text"
              placeholder="FIRST NAME"
              name="Firstname"
              value={SignUpInfo.Firstname}
              onChange={handleSignUp}
            />

            <input
              className="login-input"
              type="text"
              placeholder="LAST NAME"
              name="Lastname"
              value={SignUpInfo.Lastname}
              onChange={handleSignUp}
            />

            <input
              className="login-input"
              type="text"
              placeholder="GENDER"
              name="Gender"
              value={SignUpInfo.Gender}
              onChange={handleSignUp}
            />

            <input
              className="login-input"
              type="email"
              placeholder="EMAIL"
              name="Email"
              value={SignUpInfo.Email}
              onChange={handleSignUp}
            />

            <input
              className="login-input"
              type="password"
              placeholder="PASSWORD"
              name="Password"
              value={SignUpInfo.Password}
              onChange={handleSignUp}
            />

            
            <button className="login-button" name="SignUpButton" type="submit">
              Sign Up
            </button>
            {
              (()=>
              {
                if(SignUpStat==="def")
                  return <div></div>
                else if(SignUpStat==="Use Diff Username")
                  return <div>Please try with different username</div>
                else if(SignUpStat==="Use Diff Email")
                  return <div>Please try with different email</div>
                else if(SignUpStat==="Ok")
                return <div>Welcome to BuzzHub. Please Login with your credentials</div>
              })()
            }
          </form>
        </div>
        <div className="form-container sign-in-container">
          <form className="login-form" onSubmit={handleLogIn}>
            <h1>Login</h1>
            <input
              className="login-input"
              type="text"
              placeholder="Username"
              name="Username"
              value={Creds.Username}
              onChange={handleLogIn}
            />

            <input
              className="login-input"
              type="password"
              placeholder="Password"
              name="Password"
              value={Creds.Password}
              onChange={handleLogIn}
            />
            <button className="login-button" type="submit">
              Log In
            </button>
            {LogInStat ? <div></div> : <p>Please LogIn with Correct Credentials</p>}
      
          </form>
          
        </div>
        <div className="overlay-container">
          <div className="overlay">
            <div className="overlay-panel overlay-left">
              <button
                className="login-button"
                id="signIn"
                onClick={() => setaddclass("")}
              >
                GO TO LOGIN
              </button>
            </div>
            <div className="overlay-panel overlay-right">
              <button
                className="login-button"
                id="signUp"
                onClick={() => setaddclass("right-panel-active")}
              >
                GO TO REGISTER
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default SignUpLogIn;
