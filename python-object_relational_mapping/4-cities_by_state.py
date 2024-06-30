#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Check if all arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL database
    try:
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=username, passwd=password, db=database)
        cursor = db.cursor()

        # Execute the query to fetch cities with their states
        cursor.execute("""
            SELECT cities.id, cities.name, states.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC
        """)

        # Fetch all rows
        rows = cursor.fetchall()

        # Print results as per the example format
        for row in rows:
            print(row)

        # Close cursor and database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)
