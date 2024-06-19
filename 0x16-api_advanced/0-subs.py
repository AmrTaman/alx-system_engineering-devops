#!/usr/bin/python3
"""
iam here
"""


import requests


def number_of_subscribers(subreddit):
    """
    this function counts number of sub
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    res = requests.get(url, allow_redirects=False)
    if res.status_code == 200:
        data = res.json()['data']
        return (data['subscribers'])
    else:
        return (0)
