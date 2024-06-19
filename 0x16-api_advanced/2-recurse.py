#!/usr/bin/python3
"""
iam here
"""


import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    """
    iam here
    """
    print("dd")
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'after': after, 'limit': 100, 'count': count}
    headers = {'User-agent': 'python-requests/2.22.0'}
    resp = requests.get(url, params=params,
                        headers=headers, allow_redirects=False)
    if resp.status_code == 404:
        return None
    if resp.status_code == 200:
        data = resp.json()
        posts = data['data']['children']
        after = data['data']['after']
        count += data['data'].get("dist")
        for post in posts:
            title = post['data']['title']
            hot_list.append(title)
        if after is not None:
            recurse(subreddit, hot_list, after, count)
        return hot_list
