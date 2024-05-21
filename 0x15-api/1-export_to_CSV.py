#!/usr/bin/python3
"""
API fetching data
"""

if __name__ == "__main__":
    import csv
    import requests
    import sys

    employee_id = sys.argv[1]
    r_user = requests.get("https://jsonplaceholder.typicode.com"
                          "/users/{}".format(employee_id))
    name = r_user.json().get('name')
    r_todo = requests.get("https://jsonplaceholder.typicode.com"
                          "/todos?userId={}".format(employee_id))
    todo_data = r_todo.json()
    with open("{}.csv".format(employee_id), 'w') as f:
        csv_writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for i in todo_data:
            csv_writer.writerow([employee_id, name, task['completed'],
                                 task['title']])
