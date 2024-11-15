import sqlite3

#connecting to db, creates db
connection = sqlite3.connect("contacts.db")

# create a db cursor
cursor = connection.cursor

# create table 
cursor.execute("""
    CREATE TABLE contacts (
    firstname,
    lastname,
    email)


""" )