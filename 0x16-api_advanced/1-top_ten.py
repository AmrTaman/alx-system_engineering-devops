#!/usr/bin/python3
"""
iam here
"""


import requests


def top_ten(subreddit):
    """
    retrieves top 10 hot posts
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    params = {'limit': 10}
    headers = {'User-agent': 'python-requests/2.22.0'}
    resp = requests.get(url, params=params,
                        headers=headers, allow_redirects=False)
    if resp.status_code == 404:
        print("None")
        return
    if resp.status_code == 200:
        posts_lst = resp.json()['data']['children']
        for post in posts_lst:
            data = post['data']
            print(data['title'])
