#!/usr/bin/python3
"""
A script that retrieves and prints all records from the states table in the hbtn_0e_0_usa database.

Usage:
    ./0-select_states.py <mysql username> <mysql password> <database name>
"""

import sys
import MySQLdb

def main():
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py <username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        # Connect to MySQL database
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL DB: {e}")
        sys.exit(1)

    try:
        # Create cursor object to execute queries
        cursor = db.cursor()

        # Execute query to fetch all records from states table, sorted by id
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        rows = cursor.fetchall()

        # Print fetched rows
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error fetching data from MySQL: {e}")
        sys.exit(1)

    finally:
        # Close cursor and database connection
        cursor.close()
        db.close()

if __name__ == "__main__":
    main()

