#!/usr/bin/python3
"""
API fetching data
"""

if __name__ == "__main__":
    import requests
    import sys

    all_task_c = 0
    tasks_done = 0
    employee_id = sys.argv[1]
    r_user = requests.get("https://jsonplaceholder.typicode.com"
                          "/users/{}".format(employee_id))
    name = r_user.json().get('name')
    r_todo = requests.get("https://jsonplaceholder.typicode.com"
                          "/todos?userId={}".format(employee_id))
    todo_data = r_todo.json()
    with open("{}.csv".format(employee_id), 'w') as f:
       for i in todo_data:
            f.write('"{}","{}","{}","{}"\n'.format(employee_id, name,
                                                   i['completed'], i['title']))
