#!/usr/bin/python3
"""top_ten function Module"""
import requests


def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first
    10 hot posts listed for `subreddit`"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
            'User-Agent': 'Mozilla/5.0'
    }

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    reddit_data = response.json()

    if "data" not in reddit_data:
        print(None)
    else:
        subreddit_children = reddit_data.get("data").get("children")
        for i in range(10):
            print(subreddit_children[i].get("data").get("title"))
