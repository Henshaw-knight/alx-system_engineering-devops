#!/usr/bin/python3
""" Exports data to JSON format """
import json
import requests


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"

    response = requests.get("{}/users".format(
        base_url))
    users = response.json()

    user_ids = [data.get("id") for data in users]
    all_users = {}

    for id in user_ids:
        response = requests.get("{}/users/{}".format(
            base_url, id))
        username = response.json().get("username")

        response = requests.get("{}/users/{}/todos".format(
            base_url, id))
        todos = response.json()
        todos_copy = todos[:]

        for data in todos_copy:
            data.pop("userId")
            data.pop("id")
            data["username"] = username
            data["task"] = data.get("title")
            data["temp"] = data.get("completed")
            data.pop("completed")
            data.pop("title")
            data["completed"] = data["temp"]
            data.pop("temp")

        all_users[f"{id}"] = todos_copy

    file_path = "todo_all_employees.json"
    with open(file_path, 'w') as json_file:
        json.dump(all_users, json_file)
