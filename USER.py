#tempDb.py
#Dictionary format temp db until we decided on postgres or whatever
from datetime import datetime
import API

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))
    

#user info DB in a username:password format
USERNAME = ['admin', 'william', 'Elise']
PASSWORD = ['password', 'pwd1994', 'pass1997']

def getUSER(username, password): #take username and password as args for USER getter function

    #print out args
    print(username)
    print(password)
    stringy = ""

    for i in len(USERNAME): #loop for the length of the list of USERNAME
        if (username == USERNAME, password == PASSWORD): #if they match in the list
            print("You have entered proper credentials: logging in..")
            break
        elif():
            print("Credentials entered are not in our list of users")
        stringy = USERNAME.get(i)
    
    print (stringy)
    return stringy

def SetUSER(username,password): #make a new user    
    print(username)
    print(password)
    return 0

