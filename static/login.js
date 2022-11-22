//login.js Author: William Bukowski

//set equal to data in req
var username = document.getElementById("username");
var password = document.getElementById("password");

let User = {
  "username":username,
  "password":password
};

let promise = fetch('http://127.0.0.1:8000/login');
let response = await fetch('http://127.0.0.1:8000/login', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json;charset=utf-8'
  },
  body: JSON.stringify(User)
});

if (response.ok) {
  let json = await response.json();
} else {
  alert(response.status);
}














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
.then(function(res){ console.log(res) })
.catch(function(res){ console.log(res) })


