//login.js Author: William Bukowski

//set equal to data in req
var username = document.getElementById("username")
var password = document.getElementById("password")

//want to have this execute when sign in button is pressed

loginFetch = fetch("http://127.0.0.1:8000/login",
{
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    method: "POST",
    body: JSON.stringify({username:password})
})
.then(function(res ){ console.log(res) })
.catch(function(res){ console.log(res) })

document.getElementById(loginBtn) = loginFetch