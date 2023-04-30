#!/usr/bin/python3
"""
main purpose of this script is to list all states with a `name`
starting with the letter `N` from the db `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access the db and get the states.
    """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                        passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states \
                WHERE name LIKE BINARY 'N%' \
                ORDER BY states.id ASC")
    rows = cur.fetchall()

    for row in rows:
        print(row)
