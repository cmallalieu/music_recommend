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
import UserProfile from "views/UserProfile.jsx";
import FriendsList from "views/FriendsList.jsx";
import Login from "views/Login.jsx"
import ChartsPage from "views/chart.jsx";

const dashboardRoutes = [

  {
    path: "/dashboard",
    name: "Dashboard",
    icon: "pe-7s-graph",
    component: ChartsPage,
    layout: "/user"
  },
  {
    path: "/suggestedFriends",
    name: "Suggested Friends",
    icon: "pe-7s-note2",
    component: FriendsList,
    layout: "/user"
  },
  {
    path: "/user",
    name: "User Profile",
    icon: "pe-7s-user",
    component: UserProfile,
    layout: "/user"
  },
  {
    path: "/login",
    name: "Login",
    icon: "pe-7s-unlock",
    component: Login,
    layout: "/user"
  }
];

export default dashboardRoutes;
