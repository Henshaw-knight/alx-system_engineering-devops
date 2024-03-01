#!/usr/bin/python3
""" Exports data to CSV format """
import csv
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

    csv_file_path = "{}.csv".format(user_id)

    with open(csv_file_path, 'w') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for data in todos:
            formatted_data = {
                    "USER_ID": user_id,
                    "USERNAME": username,
                    "TASK_COMPLETED_STATUS": data.get("completed"),
                    "TASK_TITLE": data.get("title")
                    }
            writer.writerow(formatted_data.values())
