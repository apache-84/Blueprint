# CMON 20250309 CSCI 375 db_queries.py
# script to run queries from frontend calls
# team requests query, for example "I need all user names"
# I provide the query: `SELECT username FROM users;`
# team member either copy/pastes or calls this script
"""
from db_queries import fetch_query

usernames = fetch_query("SELECT userename FROM USERS;")
print(usernames)
"""
# team only has to ask for SQL statements
# no overhead of API routing, Flask, or ORM

import sqlite3

DB_FILE = "../Database/blueprintdb.db"

def execute_query(query, *params):
    """Executes a given SQL query with parameters and commits."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    conn.close()

def fetch_query(query, *params):
    """Executes a given SQL query with parameters and returns the results."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()
    return results

# example
if __name__ == "__main__":
    # get all usernames
    query = "SELECT username FROM users;"
    users = fetch_query(query)
    print (users) # should output [('user1',), ('user2',)]
    