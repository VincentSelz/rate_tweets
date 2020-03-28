from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

import itertools as it
import csv


author = 'Your name here'

doc = """
Your app description
"""

def make_field(choice):
    return models.StringField(
        choices=choice,
        label="",
        widget=widgets.RadioSelectHorizontal,
    )

def get_embed_tweet(url)
'''returns embeded html as String'''
    # importing the requests library
    import requests

    # api-endpoint
    URL = "https://publish.twitter.com/oembed"#"?buttonType=HashtagButton&query=asdfasdf&widget=Button"

    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'url': url,
        'buttonType': 'HashtagButton',
        'hide_thread': 'false'}

    # sending get request and saving the response as response object
    r = requests.get(url = URL, params = PARAMS)

    # extracting data in json format
    data = r.json()

    return data['html']

def get_tweets():
    import time
    with open('data/example_corona_tweets.tsv', newline='') as f:
       reader = csv.reader(f)
       data = list(reader)
       # tweets = []
       # for tweet in data:
       #     tweets.append(get_embed_tweet(tweet['url']))
       #     time.sleep(0.2)  #wait to not get banned
       # data = tweets
       return set(map(tuple, data))

class Constants(BaseConstants):
    name_in_url = 'rate_tweets'
    players_per_group = None
    num_rounds = 10
    q_per_round = 10
    positive =[["Negativ","Negativ"],["Neutral","Neutral"],["Positiv","Positiv"]]
    optimistic = [["Pessimistisch","Pessimistisch"],["Neutral","Neutral"],["Optimistisch","Optimistisch"]]
    happiness = [["Verärgert","Verärgert"],["Neutral","Neutral"],["Zufrieden","Zufrieden"]]
    emotional = [["Sachlich","Sachlich"],["Neutral","Neutral"],["Emotional","Emotional"]]
    tweets = get_tweets()

class Subsession(BaseSubsession):
    def set_sample(self):
        #sample = set()
        sample = ''
        try:
            #sample.add(Constants.tweets.pop()[0])
            sample = Constants.tweets.pop()[0]
            print(sample)
        except KeyError:
            print('No more tweets to distribute.')
        #index = range(len(sample))
        return str(sample) #dict(zip(index, sample))

    def creating_session(self):
        for p in self.get_players():
            #p.participant.vars['sample'] = self.set_sample()
            p.tweet = self.set_sample()

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    tweet = models.StringField()
    rating = make_field(Constants.positive)
