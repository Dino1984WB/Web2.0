//login.js Author: William Bukowski

//set equal to data in req
var username = document.getElementById("username");
var password = document.getElementById("password");

loginBtn.addEventListener("click", function() {
  
    console.log("button pressed for login")
    let promise = fetch('http://127.0.0.1:8000/login');
    let response = fetch('http://127.0.0.1:8000/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json;charset=utf-8'
      },
      body: JSON.stringify(username, password)
    });

    if (response.ok) {
      let json = response.json();
    } else {
      alert(response.status);
    }
      
});