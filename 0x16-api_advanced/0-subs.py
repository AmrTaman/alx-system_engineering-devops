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
    res = requests.get(url)
    full_data = res.json()
    data = full_data['data']
    if 'subscribers' not in data:
        return (0)
    else:
        return (data['subscribers'])
