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


def get_df_of_tweets(datafile):
    """Reads in twitter urls and gives out html to embeded tweets.

    Args: CSV-file name in folder original_data as a string.
    Out: CSV-file named as html_CSV-file in folder data.
    Notes: Reads in CSV-file, converts into DataFrame singles out urls and request
    embedded tweets from publish twitter, then saves them as html in a new CSV-file.
    """
    with open('original_data/{}'.format(datafile), newline='') as f:
       reader = pd.read_csv(f)
       urls = reader.permalink.tolist()
       tweets = []
       for tweet in urls:
           try:
               tweets.append(get_embed_tweet(tweet))
               #time.sleep(0.1)  #wait to not get banned
           except Exception:
               print('this tweet cannot be displayed.')
               pass
       df = pd.DataFrame(tweets)
       return df.to_csv('data/_html'+str(len(tweets))+'_{}'.format(datafile), index=False)

get_df_of_tweets("selected_tweets_for_labeling.csv")
