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
    all_tasks = len(todo_data)
    done_tasks = [task for task in todo_data if task['completed']]
    done_tasks_num = len(done_tasks)
    print("Employee {} is done with tasks"
          "({}/{}):".format(name, done_tasks_num, all_tasks))
    for task in done_tasks:
        print("\t {}".format(task['title']))
