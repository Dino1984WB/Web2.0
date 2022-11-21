#tempDb.py
#Dictionary format temp db until we decided on postgres or whatever
from datetime import datetime
from flask import abort

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))
    
def getFormattedUSER():
    for i in next(USER, None):
        return (i)

#user info DB in a username:password format
USER = {
    "admin":"password",
    "MICKEY":"MOUSE",
    "SCOOBY":"DOO",
    "SPIDER":"MAN"
}

def getUSER():
    stringy = USER.get(0)
    print (stringy)
    return stringy

getUSER()
