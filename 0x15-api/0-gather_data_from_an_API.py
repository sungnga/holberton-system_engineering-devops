#!/usr/bin/python3
"""
A Python script using a REST API, for a given employee ID,
returns information about his/her TODO list progress
"""

import requests
import sys


if __name__ == "__main__":
    users = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                         .format(sys.argv[1]))
    todos = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(sys.argv[1]))
    dict_users = users.json()
    dict_todos = todos.json()
    comp_tasks = 0
    tasks = 0
    for i in dict_todos:
        if i.get('completed') is True:
            comp_tasks += 1
        else:
            tasks += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(dict_users['name'], comp_tasks, tasks + comp_tasks))
    for i in dict_todos:
        if i.get('completed') is True:
            print('\t {}'.format(i.get('title')))
