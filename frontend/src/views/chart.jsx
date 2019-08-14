import React from "react";
import { Bar } from "react-chartjs-2";
import { MDBContainer } from "mdbreact";

class ChartsPage extends React.Component {
  state = {
    dataBar: {
      labels: [
        'San Holo',
        'Kanye West',
        'J. Cole',
        'Led Zeppelin',                                                                                             
        'Pink Floyd',
        'Mac Miller', 
        'Jimi Hendrix',                                                                                            
        'Flume',
        'MGMT',
        'Portugal. The Man',                                                                                            
        'Bon Iver',                                                                                             
        'Kendrick Lamar',
        'Eminem',                                                                                             
        'Vampire Weekend',
        'GRiZ',        
        'Cage The Elephant',                                                                                     
        'The Strokes',                                                                                             
        'Chance the Rapper',
        'SMLE',
        'Louis The Child', 
        'Jai Wolf',                                                                                           
        'Petit Biscuit',                                                                                             
        'NoMBe',                                                                                             
        'Tame Impala',                                                                                             
        'ODESZA'                                                                                          
      ],
      datasets: [
        {
          label: "Rating",
          data: [36, 35, 34, 33, 33, 32, 32, 31, 31, 30, 30, 29, 29, 28, 28, 27, 27, 26, 26, 25, 25, 24, 24, 23, 22],
          backgroundColor: [
            
            "rgba(235, 0, 0, 1)",
            "rgba(235, 102, 0, 1)",
            "rgba(235, 180, 0, 1)",
            "rgba(235, 235, 0, 1)",
            "rgba(156, 235, 0, 1)",
            "rgba(51, 235, 0, 1)",
            "rgba(0, 235, 231, 1)",
            "rgba(0, 156, 235, 1)",
            "rgba(0, 59, 235, 1)",
            "rgba(98, 0, 235, 1)",
            "rgba(156, 0, 235, 1)",
            "rgba(235, 0, 231, 1)",
            "rgba(235, 0, 149, 1)",
            "rgba(235, 0, 86, 1)",
            "rgba(235, 0, 0, 1)",
            "rgba(235, 0, 0, 0.4)",
            "rgba(235, 102, 0, 0.4)",
            "rgba(235, 180, 0, 0.4)",
            "rgba(235, 235, 0, 0.4)",
            "rgba(156, 235, 0, 0.4)",
            "rgba(51, 235, 0, 0.4)",
            "rgba(0, 235, 231, 0.4)",
            "rgba(0, 156, 235, 0.4)",
            "rgba(0, 59, 235, 0.4)",
            "rgba(98, 0, 235, 0.4)",
            "rgba(255, 134,159,0.4)",
            "rgba(98,  182, 239,0.4)",
            "rgba(255, 218, 128,0.4)",
            "rgba(113, 205, 205,0.4)",
            "rgba(170, 128, 252,0.4)",
            "rgba(255, 177, 101,0.4)"
          ],
          borderWidth: 2,
        //   borderColor: [
        //     "rgba(255, 134, 159, 1)",
        //     "rgba(98,  182, 239, 1)",
        //     "rgba(255, 218, 128, 1)",
        //     "rgba(113, 205, 205, 1)",
        //     "rgba(170, 128, 252, 1)",
        //     "rgba(255, 177, 101, 1)"
        //   ]
        }
      ]
    },
    barChartOptions: {
      responsive: false,
      maintainAspectRatio: false,
      scales: {
        xAxes: [
          {
            barPercentage: 1,
            gridLines: {
              display: true,
              color: "rgba(0, 0, 0, 0.1)"
            }
          }
        ],
        yAxes: [
          {
            gridLines: {
              display: true,
              color: "rgba(0, 0, 0, 0.1)"
            },
            ticks: {
              beginAtZero: true
            }
          }
        ]
      }
    }
  }


  render() {
    return (
      <MDBContainer>
        <h3 className="mt-5">25 Favorite Artists Generated from Spotify Data <br></br> A Full List of Artists is Used to Match Users</h3>
        <Bar data={this.state.dataBar} options={this.state.barChartOptions} height={800} width={1200}/>
      </MDBContainer>
    );
  }
}

export default ChartsPage;