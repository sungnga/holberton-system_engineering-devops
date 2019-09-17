#!/usr/bin/python3
"""
Extend Task 0 Python script to export data in the csv format
"""

import requests
import sys
import csv


if __name__ == "__main__":
    dict_users = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'
        .format(sys.argv[1])).json()
    dict_todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'
        .format(sys.argv[1])).json()

    with open('{}.csv'.format(sys.argv[1]), 'w') as csvfile:
        todowriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for i in dict_todos:
            todowriter.writerow([i.get('userId'),
                                 dict_users.get('username'),
                                 i.get('completed'),
                                 i.get('title')])
