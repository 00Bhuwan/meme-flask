from flask import Flask
import requests
import json


def get_meme():
    # url = "https://meme-api.herokuapp.com/gimme"
    # response = json.loads(requests.request("GET", url).text)
    # meme_large = response["preview"][-2]
    # subreddit = response["subreddit"]
    # return meme_large, subreddit
    url = "https://meme-api.herokuapp.com/gimme"
    response = requests.get(url, timeout=5)

    if response.status_code != 200:
        return None, "API error"

    data = response.json()

    meme_large = data["preview"][-2]
    subreddit = data["subreddit"]
    return meme_large, subreddit