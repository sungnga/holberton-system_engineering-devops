#!/usr/bin/python3
"""
Extend Task 0 Python script to export data in json format
"""

import csv
import json
import requests
import sys


if __name__ == "__main__":
    users = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                         .format(sys.argv[1])).json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(sys.argv[1])).json()
    todo_list = []
    for i in todos:
        todo = {}
        todo["task"] = i.get("title")
        todo["completed"] = i.get("completed")
        todo["username"] = users.get("username")
        todo_list.append(todo)
    dict = {sys.argv[1]: todo_list}
    with open('{}.json'.format(sys.argv[1]), 'w') as jsonfile:
        json.dump(dict, jsonfile)
