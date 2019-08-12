import React from "react";
import ReactDOM from "react-dom";
import SpotifyLogin from 'react-spotify-login';


class Login extends React.Component {

    constructor(props){
      super(props);
      this.state = { 
          username : ''
      };
    }
    
    onSuccess = response => console.log(response);
    onFailure = response => console.error(response);
    // }

    render() {
        return (
          <SpotifyLogin clientId='98024be3f43d40aa82643d244f9a35c8'
          redirectUri='http://localhost:8888/callback'/>,
        document.getElementById('example')
      );
    }
 

   
//     onSubmit = event => {
//         event.preventDefault();
//         const username = this.username.value;
//         const info = {username : username};
//         this.setState(
//             info
//         )
//         localStorage.setItem('username', username);

//         console.log(localStorage.getItem('username'))
//     };
   
//     render() {
//       return (
//         <React.Fragment>
//             <form className="form-inline" onSubmit={this.onSubmit}>
//                 <input
//                     type="text"
//                     className="form-control mb-2 mr-sm-2 mb-sm-0"
//                     placeholder="Enter your Spotify username"
//                     ref={input => this.username = input}/>
//                 <button 
//                     type="submit" 
//                     className="btn btn-primary">Submit
//                 </button>
//             </form>
//         </React.Fragment>
//       );
//     }
   }

   export default Login;

   ReactDOM.render(<Login />, document.getElementById('challenge-node'))

// class Application extends React.Component {

//     constructor(props) {
//       super(props);
//       this.state = {
//         data: [
//           {
//             username : ''
//           },
//         ]
//       }
//     }
  
//     onSubmit = event => {
//       event.preventDefault();
//       const username = this.username.value;
//       const info = {usernamename: username};
//       const data = [info];
//       this.setState({
//         data: data
//       });
//     };
  
//     render() {
//       return (
//           <div className="container">
//             <h1>React State</h1>
  
//             <hr/>
  
//             <div className="row">
//               <form className="form-inline" onSubmit={this.onSubmit}>
//                 <input
//                     type="text"
//                     className="form-control mb-2 mr-sm-2 mb-sm-0"
//                     placeholder="Name"
//                     ref={input => this.name = input}/>
//                 <div className="input-group mb-2 mr-sm-2 mb-sm-0">
//                   <input
//                       type="text"
//                       className="form-control"
//                       placeholder="Age"
//                       ref={input => this.age = input}/>
//                 </div>
//                 <button type="submit" className="btn btn-primary">Save</button>
//               </form>
//             </div>
  
//             <hr/>
  
//             <div className="row">
//               {
//                 this.state.data.map((info, index) => <Card key={index} info={info}/>)
//               }
//             </div>
  
//           </div>
//       )
//     }
//   }
  
//   const Card = props =>
//       <div className="col-md-6 col-lg-3">
//         <div className="card mb-3">
//           <div className="card-body">
//             <p className="card-title"><span>Name: </span>{props.info.name}</p>
//             <p className="card-text">
//               <span>Age: </span>{props.info.age}
//             </p>
//           </div>
//         </div>
//       </div>;

// export default Login