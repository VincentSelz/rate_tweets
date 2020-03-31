"""Reads in urls from DataFrame and returns DataFrame with the functioning html to embed tweets.
"""

import pandas as pd
import requests
import csv

def get_embed_tweet(url):
    """Reads in tweet-url returns embeded html as String
    Args: url of the tweet.
    Functionality: Reads in the URL, contacts publish twitter, extracts json
    data and returns the html.
    """
    # api-endpoint
    URL = "https://publish.twitter.com/oembed"

    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'url': url,
        'buttonType': 'HashtagButton',
        'hide_thread': 'false'}

    # sending get request and saving the response as response object
    r = requests.get(url = URL, params = PARAMS)
    # extracting data in json format
    data = r.json()

    return data['html']


def get_df_of_tweets():
    with open('data/test_data.csv', newline='') as f:
       reader = pd.read_csv(f)
       # this is the whole list (and takes ages)
       #urls = reader.tweet_url.tolist()
       # to test a short one, this does the trick
       urls = reader.tweet_url.tolist()
       tweets = []
       for tweet in urls:
           try:
               tweets.append(get_embed_tweet('https://twitter.com' + tweet))
               #time.sleep(0.1)  #wait to not get banned
           except Exception:
               print('this tweet cannot be displayed.')
               pass
       df = pd.DataFrame(tweets)
       return df.to_csv('data/html_data.csv', index=False)

get_df_of_tweets()
