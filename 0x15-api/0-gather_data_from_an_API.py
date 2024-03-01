#!/usr/bin/python3
""" Script that, for a given emplyee ID, returns information
about his/her TODO list progress. """
import requests
from sys import argv


if __name__ == "__main__":
    employee_id = argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    response = requests.get("{}/users/{}".format(
        base_url, employee_id))
    employee_name = response.json().get("name")

    response = requests.get("{}/users/{}/todos".format(
        base_url, employee_id))
    todos = response.json()
    total_tasks = len(todos)
    no_of_done_tasks = 0
    done_tasks = []

    for data in todos:
        if data.get("completed") is True:
            no_of_done_tasks += 1
            done_tasks.append(data.get("title"))

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, no_of_done_tasks, total_tasks))
    for title in done_tasks:
        print("\t {}".format(title))
