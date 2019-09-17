#!/usr/bin/python3
"""
Extend Task 0 Python script to export all employee data in json format
"""

import csv
import json
import requests
import sys


if __name__ == "__main__":
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    dict = {}
    for user in users:
        todo_list = []
        todos = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'
            .format(user.get('id'))).json()
        for i in todos:
            todo = {}
            todo["task"] = i.get("title")
            todo["completed"] = i.get("completed")
            todo["username"] = user.get("username")
            todo_list.append(todo)
        dict[user.get('id')] = todo_list
    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(dict, jsonfile)
