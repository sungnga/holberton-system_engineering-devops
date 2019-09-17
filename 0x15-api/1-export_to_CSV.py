#!/usr/bin/python3
"""
Extend Task 0 Python script to export data in the csv format
"""

import csv
import requests
import sys


if __name__ == "__main__":
    users = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                         .format(sys.argv[1])).json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(sys.argv[1])).json()

    with open('{}.csv'.format(sys.argv[1]), 'w') as csvfile:
        todowriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for i in todos:
            todowriter.writerow([i.get('userId'),
                                 users.get('username'),
                                 i.get('completed'),
                                 i.get('title')])
