import React from "react";
import { Redirect } from 'react-router'

class Login extends React.Component {

    constructor(props){
      super(props);
      this.state = { 
          username : '',
          redirect : false
      };
    }
    
    onSubmit = event => {
        event.preventDefault();
        const username = this.username.value;
        const info = {username : username, redirect : true};
        this.setState(
            info
        )

        const fetchUrl =  'http://127.0.0.1:5000/api/get_chart_data/' + username
        
        fetch(fetchUrl, {mode: 'cors'})
        .then((response) => response.json())
        .then((findresponse)=> {
          console.log(findresponse)
          sessionStorage.setItem('data', findresponse)
        })


        
       // <ul>{this.state.data.map(item => <li>{item.title}</li>)} </ul>

        sessionStorage.setItem('username', username);

        console.log(sessionStorage.getItem('username'))
        console.log(sessionStorage.getItem('data'))

       
    };
   
    render() {

      if (this.state.redirect) {
        return <Redirect to="/user/dashboard" />
      }

      return (
        <React.Fragment>
          <form className="form-inline" onSubmit={this.onSubmit}>
              <input
                  type="text"
                  className="form-control mb-2 mr-sm-2 mb-sm-0"
                  placeholder="Spotify Username"
                  ref={input => this.username = input}/>
              <button 
                  type="submit" 
                  className="btn btn-primary">Submit
              </button>
          </form>
        </React.Fragment>
      );
    }
   }

   export default Login;