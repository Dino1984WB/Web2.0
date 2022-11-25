#API.py Author William Bukowski, usese Flask
import USER
import dbC
import dbInit
from flask import Flask, render_template, request
from flask_restful import Api, Resource
from flask import render_template # Remove: import Flask
import connexion
import psycopg2
import os

#NEW FLASK APP
app=Flask(__name__, static_folder='static/', static_url_path='')#Flask app init


#app = connexion.App(__name__, specification_dir="./") #new connection to flask app
#app.add_api("swagger.yaml") #add the api config file yaml


#routes
@app.route('/', methods=['GET', 'POST'])
def landingPage():
    return render_template("landingPage.html")


@app.route("/login")
def login():
    connC = dbC.getConnectionUSERS() #make connection to postgres db 'Flask'
    connC.execute(querySelect)
    
    #grab the username, password from the post body, plug into getUSER(arg,arg)
    username = "admin" #make this var equal to the text in the html box on login page, username
    password = "password"
    admin = USER.getUSER(username, password)
    print(admin)    
    
    return render_template("login.html")


@app.route("/home")
def home():
    return render_template("home.html")


if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=8000, debug=True) #run app