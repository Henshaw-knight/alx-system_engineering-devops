#!/usr/bin/python3
""" Exports data to JSON format """
import json
import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    response = requests.get("{}/users/{}".format(
        base_url, user_id))
    username = response.json().get("username")

    response = requests.get("{}/users/{}/todos".format(
        base_url, user_id))
    todos = response.json()
    todos_copy = todos[:]

    user_details = {}
    file_path = "{}.json".format(user_id)

    for data in todos_copy:
        data["task"] = data.get("title")
        data["temp"] = data.get("completed")
        data.pop("title")
        data.pop("completed")
        data.pop("userId")
        data.pop("id")
        data["completed"] = data["temp"]
        data["username"] = username
        data.pop("temp")

    user_details[f"{user_id}"] = todos_copy

    with open(file_path, 'w') as json_file:
        json.dump(user_details, json_file)
