#!/usr/bin/python3
"""Module that contains function that queries the Reddit API
and returns the number of subscribers of a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    for `subreddit`"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
            'User-Agent': 'Mozilla/5.0'
    }

    response = requests.get(url, headers=headers)
    reddit_data = response.json()

    try:
        subscribers = reddit_data.get("data").get("subscribers")
        return subscribers
    except Exception:
        return 0
