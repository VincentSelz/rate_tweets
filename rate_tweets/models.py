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

import itertools
import csv
import random
import pandas as pd
import requests
import time


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
def extend_treatment(list_of_lists):
    treat = []
    for list in list_of_lists:
        treat.extend(10*list)
    return treat

def get_embed_tweet(url):
    '''returns embeded html as String'''

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

    with open('data/test_data.csv', newline='') as f:
       reader = pd.read_csv(f)
       urls = reader.tweet_url.tolist()
       urls[-1]
       reader
def get_tweets():
    with open('data/test_data.csv', newline='') as f:
       reader = pd.read_csv(f)
       # this is the whole list
       #urls = reader.tweet_url.tolist()
       # to test a short one does the trick
       urls = reader.tweet_url.head(200).tolist()
       tweets = []
       for tweet in urls:
           try:
               tweets.append(get_embed_tweet('https://twitter.com' + tweet))
               #time.sleep(0.1)  #wait to not get banned
               print ('one more')
           except Exception:
               print('this tweet cannot be displayed.')
               pass


       print(tweets[0])
       return set(tweets)

class Constants(BaseConstants):
    name_in_url = 'rate_tweets'
    players_per_group = None
    num_participants = 4
    num_rounds = 40
    q_per_round = 10
    positive =[["Negativ","Negativ"],["Neutral","Neutral"],["Positiv","Positiv"]]
    optimistic = [["Pessimistisch","Pessimistisch"],["Neutral","Neutral"],["Optimistisch","Optimistisch"]]
    happiness = [["Verärgert","Verärgert"],["Neutral","Neutral"],["Zufrieden","Zufrieden"]]
    emotional = [["Sachlich","Sachlich"],["Neutral","Neutral"],["Emotional","Emotional"]]
    choices = [['positive'], ['optimistic'], ['happiness'], ['emotional']]
    treatment_cycles = []
    for i in range(num_participants):
        shuffled_rating = random.sample(choices, len(choices))
        real_treatments = extend_treatment(shuffled_rating)
        treatment_cycle = itertools.cycle(real_treatments)
        treatment_cycles.append(treatment_cycle)


    #def get_tweets():
    #    with open('data/example_corona_tweets.tsv', newline='') as f:
    #       reader = csv.reader(f)
    #       data = list(reader)
    #    return set(map(tuple, data))
    #tweets = get_tweets()
    #def get_tweet_text():
    #    with open('data/test_data.csv', newline='') as f:
    #        reader = pd.read_csv(f)
    #    text = reader.text.tolist()
    #    return text
    #tweets = get_tweet_text()
    tweets = get_tweets()

class Subsession(BaseSubsession):
    def set_sample(self):
        #shuffled_tweets = random.sample(Constants.tweets,len(Constants.tweets))
        #tweet_cycle = itertools.cycle(shuffled_tweets)
        sample = ''
        try:
            sample = Constants.tweets.pop()
            #sample = next(tweet_cycle)
            print(sample)
        except KeyError:
            print('No more tweets to distribute.')
        return str(sample)

    def creating_session(self):
        count = 0
        for p in self.get_players():
            p.treatment = next(Constants.treatment_cycles[count])
            p.tweet = self.set_sample()
            count += 1

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    tweet = models.StringField()
    treatment = models.StringField()
    rating = make_field(Constants.positive)
    pos_rating = make_field(Constants.positive)
    opt_rating = make_field(Constants.optimistic)
    hap_rating = make_field(Constants.happiness)
    emo_rating = make_field(Constants.emotional)
