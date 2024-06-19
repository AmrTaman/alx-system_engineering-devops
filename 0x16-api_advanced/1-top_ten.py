#!/usr/bin/python3
"""
iam here
"""


import requests


def top_ten(subreddit):
    """
    retrieves top 10 hot posts
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    resp = requests.get(url, allow_redirects=False)
    if resp.status_code == 200:
        posts_lst = resp.json()['data']['children']
        for post in posts_lst:
            data = post['data']
            print(data['title'])
    else:
        print("None")
