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
    params = {
            'limit': 10
    }

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    reddit_data = response.json()

    if "data" not in reddit_data:
        print(None)
    else:
        subreddit_children = reddit_data.get("data").get("children")
        for child in subreddit_children:
            print(child.get("data").get("title"))
