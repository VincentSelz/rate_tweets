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
        blank=True,
    )
def extend_treatment(list_of_lists):
    treat = []
    for list in list_of_lists:
        treat.extend(10*list)
    return treat

def get_tweets(datafile):
    """Reads in datafile with html and returns them as a list.

    Args: datafile in folder data as string.
    Out: list of htmls.
    """
    with open('data/{}'.format(datafile), newline='') as f:
       reader = pd.read_csv(f)
       tweets = reader['0'].tolist()
       return tweets

class Constants(BaseConstants):
    name_in_url = 'rate_ratings'
    players_per_group = None
    num_participants = 4
    num_rounds = 40

    #Choices for different StringFields
    pos_scale =[["Negativ/Positiv","Negativ/Positiv"]]
    opt_scale = [["Pessimistisch/Optimistisch","Pessimistisch/Optimistisch"]]
    hap_scale = [["Verärgert/Zufrieden","Verärgert/Zufrieden"]]
    emo_scale = [["Sachlich/Emotional","Sachlich/Emotional"]]
    not_applicable = [["Nicht zutreffend", "Nicht zutreffend"]]
    choices = [['positive'], ['optimistic'], ['happiness'], ['emotional']]

    # Get tweets from precurated sample
    tweets = get_tweets("html_test_data.csv")

    tweet_cycles = []
    for i in range(num_participants):
        # Makes personalized random cycle of tweets
        shuffled_tweets = random.sample(tweets, len(tweets))
        # Turns tweets into cycles and stores them in a list.
        tweet_cycle = itertools.cycle(shuffled_tweets)
        tweet_cycles.append(tweet_cycle)

class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.tweet = next(Constants.tweet_cycles[count])


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    tweet = models.StringField()
    pos_scale = make_field(Constants.pos_scale)
    opt_scale = make_field(Constants.opt_scale)
    hap_scale = make_field(Constants.hap_scale)
    emo_scale = make_field(Constants.emo_scale)
    not_applicable = make_field(Constants.not_applicable)
