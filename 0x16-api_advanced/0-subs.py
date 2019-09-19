#!/usr/bin/python3
"""A function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given subreddit"""

import requests
import json


def number_of_subscribers(subreddit):
    """returns the number of subscribers from the Reddit API"""
    r = requests.get(r'http://www.reddit.com/r/{}/about.json'
                     .format(subreddit), headers={'User-agent': 'x'})
    json = r.json()
    data = json.get('data')
    if data:
        return data.get('subscribers')
    else:
        return 0
