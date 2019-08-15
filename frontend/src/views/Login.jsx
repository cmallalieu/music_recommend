import React from "react";
import { Redirect } from 'react-router'
import {
  Grid,
  Row,
  Col,
} from "react-bootstrap";

import { Card } from "components/Card/Card.jsx";
import { FormInputs } from "components/FormInputs/FormInputs.jsx";


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
        const username = 'ic2uyujb93pc2hj6hpfibmnkp';
        const info = {username : username, redirect : true};
        this.setState(
            info
        )

        console.log(username)

        const fetchUrl =  'http://165.22.188.156:8080/api/get_chart_data/' + username
        
        fetch(fetchUrl, {mode: 'cors'})
        .then((response) => response.json())
        .then((findresponse)=> {
          sessionStorage.setItem('artistName', findresponse['artistName'])
          sessionStorage.setItem('rating', findresponse['rating'])
        })


        sessionStorage.setItem('username', username);
        

        // console.log(sessionStorage.getItem('username'))
        // console.log(sessionStorage.getItem('data'))

       
    };
   
    render() {

      if (this.state.redirect) {
        return <Redirect to="/user/dashboard" />
      }

      return (


        <div className="content">
        <Grid fluid>
          <Row>
            <Col md={8}>
              <Card
                title="Login"
                content={
                  <form onSubmit={this.onSubmit}>
                    <FormInputs
                      ncols={["col-md-12"]}
                    
                      properties={[
                        {
                          label: "Spotify Username",
                          type: "text",
                          bsClass: "form-control",
                          placeholder: "Username",
                          defaultValue: '',
                          
                        },
                      ]}
                      ref={input => this.username = FormInputs}
                      />                    
                    <button 
                      type="submit" 
                      className="btn btn-primary">Submit
                    </button>
                  </form>
                }
              />
            </Col>
          </Row>
        </Grid>
      </div>
    );
  }
}
    //     <React.Fragment>
    //       <form className="form-inline" onSubmit={this.onSubmit}>
    //           <input
    //               type="text"
    //               className="form-control mb-2 mr-sm-2 mb-sm-0"
    //               placeholder="Spotify Username"
    //               ref={input => this.username = input}/>
    //           <button 
    //               type="submit" 
    //               className="btn btn-primary">Submit
    //           </button>
    //       </form>
    //     </React.Fragment>
    //   );
    // }
   //}

   export default Login;