#API.py Author William Bukowski, usese Flask
from flask import Flask, render_template, request
from flask_restful import Api, Resource
from flask import render_template # Remove: import Flask
import connexion
import USER

#json test data
data = {"username":"admin", "password":"password"} #some json data for tests

#app init
app=Flask(__name__) #new Flask app

#
app = connexion.App(__name__, specification_dir="./") #new connection to flask app
app.add_api("swagger.yaml") #add the api config file yaml



#routes
@app.route('/', methods=['GET', 'POST'])
def landingPage():
    return render_template("landingPage.html")


@app.route("/login")
def login():
    #grab the usrname, passwrod from the post body, plug into getUSER(arg,arg)
    username = "admin"
    password = "password"

    USER.getUSER(username, password)    

    return render_template("login.html")

@app.route("/home")
def home():
    return render_template("home.html")


if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=8000, debug=True) #run app