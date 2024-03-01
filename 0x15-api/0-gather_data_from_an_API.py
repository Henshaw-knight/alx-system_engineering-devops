#!/usr/bin/python3
""" Script that, for a given emplyee ID, returns information
about his/her TODO list progress. """
import requests
from sys import argv


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    employee_id = argv[1]

    response = requests.get(f"{base_url}/users/{employee_id}")
    employee_name = response.json().get("name")

    response = requests.get(f"{base_url}/users/{employee_id}/todos")
    todos = response.json()
    total_tasks = len(todos)
    no_of_done_tasks = 0
    done_tasks = []

    for data in todos:
        if data.get("completed") is True:
            no_of_done_tasks += 1
            done_tasks.append(data.get("title"))

    print(f"Employee {employee_name} is done with \
tasks({no_of_done_tasks}/{total_tasks}):")
    for title in done_tasks:
        print(f"\t {title}")
