/*!

=========================================================
* Light Bootstrap Dashboard React - v1.3.0
=========================================================

* Product Page: https://www.creative-tim.com/product/light-bootstrap-dashboard-react
* Copyright 2019 Creative Tim (https://www.creative-tim.com)
* Licensed under MIT (https://github.com/creativetimofficial/light-bootstrap-dashboard-react/blob/master/LICENSE.md)

* Coded by Creative Tim

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

*/
import React from "react";
import {
  Grid,
  Row,
  Col,
} from "react-bootstrap";

import { Card } from "components/Card/Card.jsx";
import { FormInputs } from "components/FormInputs/FormInputs.jsx";
import { UserCard } from "components/UserCard/UserCard.jsx";

class UserProfile extends React.Component {

  constructor(props){
    super(props);
    this.state = { 
        username : '',
        name : '',
        email : '',
        spotify : '',
        image : ''
    };
  }

  componentWillMount() {
    
    const username = sessionStorage.getItem('username')
    const fetchUrl = "http://127.0.0.1:5000/api/get_user_profile/" + username

    fetch(fetchUrl, {mode: 'cors'})
    .then((response) => response.json())
    .then((findresponse)=> {
      const name = findresponse['display_name']
      const spotify = findresponse['external_urls']['spotify']
      const username = findresponse['id']
      const image = findresponse['images']['0']['url']

      const info = {
        username : username,
        name : name,
        email : 'cpm220@lehigh.edu',
        spotify : spotify,
        image : image
      }

      this.setState(
        info
      )
    })
  }


  render() {
    
    const username = this.state.username
    const name = this.state.name
    const spotify = this.state.spotify
    const email = this.state.email

    return (
      <div className="content">
        <Grid fluid>
          <Row>
            <Col md={8}>
              <Card
                title="Profile"
                content={
                  <form>
                    <FormInputs
                      ncols={["col-md-6", "col-md-6"]}
                    
                      properties={[
                        {
                          label: "Username",
                          type: "text",
                          bsClass: "form-control",
                          placeholder: "Username",
                          defaultValue: username
                        },
                        {
                          label: "Email address",
                          type: "email",
                          bsClass: "form-control",
                          placeholder: "Email",
                          defaultValue: email
                        }
                      ]}
                    />
                    <FormInputs
                      ncols={["col-md-6", "col-md-6"]}
                      properties={[
                        {
                          label: "First name",
                          type: "text",
                          bsClass: "form-control",
                          placeholder: "Name",
                          defaultValue: name
                        },
                        {
                          label: "Spotify URL",
                          type: "text",
                          bsClass: "form-control",
                          placeholder: "Spotify URL",
                          defaultValue: spotify
                        },
                      ]}
                    />
                  </form>
                }
              />
            </Col>
            <Col md={4}>
              <UserCard
                bgImage="https://ununsplash.imgix.net/photo-1431578500526-4d9613015464?fit=crop&fm=jpg&h=300&q=75&w=400"
                avatar={this.state.image}
                name= {this.state.name}
                userName={this.state.username}
                // description={
                // }
              />
            </Col>
          </Row>
        </Grid>
      </div>
    );
  }
}

export default UserProfile;
