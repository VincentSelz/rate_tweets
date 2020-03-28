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

class Constants(BaseConstants):
    name_in_url = 'optimistic'
    players_per_group = None
    num_rounds = 10
    positive =[["Negativ","Negativ"],["Neutral","Neutral"],["Positiv","Positiv"]]
    optimistic = [["Pessimistisch","Pessimistisch"],["Neutral","Neutral"],["Optimistisch","Optimistisch"]]
    happiness = [["Verärgert","Verärgert"],["Neutral","Neutral"],["Zufrieden","Zufrieden"]]
    emotional = [["Sachlich","Sachlich"],["Neutral","Neutral"],["Emotional","Emotional"]]
    choices = [positive,optimistic,happiness,emotional]
    #def get_tweets():
    #    with open('data/example_corona_tweets.tsv', newline='') as f:
    #       reader = csv.reader(f)
    #       data = list(reader)

    #    return set(map(tuple, data))
    #tweets = get_tweets()
    def get_tweet_text():
        with open('data/test_data.csv', newline='') as f:
            reader = pd.read_csv(f)
        text = reader.text.tolist()
        return text
    tweets = get_tweet_text()


class Subsession(BaseSubsession):
    def set_sample(self):
        #sample = set()
        shuffled_tweets = random.sample(Constants.tweets,len(Constants.tweets))
        tweet_cycle = itertools.cycle(shuffled_tweets)
        sample = ''
        try:
            # Original idea works but only gives back the whole set; does not cycle.
            #sample = Constants.tweets.pop()[0]
            #has parentheses around
            sample = next(tweet_cycle)
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
    rating = make_field(Constants.optimistic)
