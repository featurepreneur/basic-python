'''
Created on 
Course work: 
@author: Ishita
Source:
    
'''
# Import necessary modules

import json
import sqlite3

con=sqlite3.connect('museum.db')

cursor= con.cursor()
cursor.execute("DROP TABLE IF EXISTS MUSEUM")
query= """CREATE TABLE MUSEUM(ID INT PRIMARY KEY NOT NULL, NAME CHAR(25) NOT NULL, COUNTRY CHAR(20) NOT NULL)"""

con.execute("INSERT INTO MUSEUM(ID, NAME, COUNTRY)""VALUES(1, 'Smithsonian Institution', 'Washington')")

con.execute("INSERT INTO MUSEUM(ID, NAME, COUNTRY)""VALUES(2, 'Le Louvre', 'Paris')")


con.commit()
con.close()

# places_query = "insert into museum(id,museum name, country,)"

# def start():

    

# if __name__== "__main__":