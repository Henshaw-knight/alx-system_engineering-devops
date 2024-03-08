#!/usr/bin/python3
"""recurse function Module"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """Queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit.
    If no resutls are found for the given subreddit, the function returns
    None
    """

    if after is None:
        return hot_list

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
            'User-Agent': 'Mozilla/5.0'
    }
    params = {
            'after': after
    }

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    reddit_data = response.json()

    try:
        after = reddit_data.get("data").get("after")
        subreddit_children = reddit_data.get("data").get("children")
        for child in subreddit_children:
            hot_list.append(child.get("title"))
        return recurse(subreddit, hot_list, after)

    except Exception:
        return None
