#!/usr/bin/python3
"""A function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given subreddit"""

import requests
import json


def number_of_subscribers(subreddit):
    """returns the number of subscribers from the Reddit API"""
    """Mozilla/5.0 (X11; CrOS x86_64 10066.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"""
    r = requests.get(r'http://www.reddit.com/r/{}/about.json'.format(subreddit), headers={'User-agent': 'x'})
    json = r.json()
    subscribers = json.get('data').get('subscribers')
    if not subscribers:
        return 0
    return subscribers
