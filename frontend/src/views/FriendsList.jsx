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
import React, { Component } from "react";
import { Grid, Row, Col, Table } from "react-bootstrap";

import Card from "components/Card/Card.jsx";
import { thArray, tdArray } from "variables/Variables.jsx";

class FriendsList extends Component {

  constructor(props){
    super(props);
    this.state = { 
        similarity : 0
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

      const info = {
        username : username,
        name : name,
        email : 'cpm220@lehigh.edu',
        spotify : spotify
      }

      this.setState(
        info
      )
    })
  }


  render() {
    return (
      <div className="content">
        <Grid fluid>
          <Row>
            <Col md={12}>
              <Card
                title="Friends List"
                ctTableFullWidth
                ctTableResponsive
                content={
                  <Table striped hover>
                    <thead>
                      <tr>
                        {thArray.map((prop, key) => {
                          return <th key={key}>{prop}</th>;
                        })}
                      </tr>
                    </thead>
                    <tbody>
                      {tdArray.map((prop, key) => {
                        return (
                          <tr key={key}>
                            {prop.map((prop, key) => {
                              return <td key={key}>{prop}</td>;
                            })}
                          </tr>
                        );
                      })}
                    </tbody>
                  </Table>
                }
              />
            </Col>
          </Row>
        </Grid>
      </div>
    );
  }
}

export default FriendsList;
