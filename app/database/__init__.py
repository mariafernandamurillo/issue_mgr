#g is the global context objetc: Is a pipe line to access data from 
# different point of the app.
from flask  import g          
import sqlite3


#A constant (it is in upprcase)
DATABASE_URL = "main.db"

#Function to get connection to a db
def get_db():
    #Looking for an attribute named database.
    #Underscor before database: it supose to be a private attribute.
    #Who can access to them. 
    db = getattr(g, "_database", None)
    if not db:
        #
        db = g._database = sqlite3.connect(DATABASE_URL)
    return db

#Singleton desgn pattern: check this. 