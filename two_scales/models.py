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
    name_in_url = 'two_scales'
    players_per_group = None
    num_participants = 100
    num_rounds = 40

    #Choices for different StringFields
    positive =[["Negativ","Negativ"],["Neutral","Neutral"],["Positiv","Positiv"],["Nicht zutreffend", "Nicht zutreffend"]]
    optimistic = [["Pessimistisch","Pessimistisch"],["Neutral","Neutral"],["Optimistisch","Optimistisch"],["Nicht zutreffend", "Nicht zutreffend"]]
    happiness = [["Verärgert","Verärgert"],["Neutral","Neutral"],["Zufrieden","Zufrieden"],["Nicht zutreffend", "Nicht zutreffend"]]
    emotional = [["Sachlich","Sachlich"],["Emotional","Emotional"],["Nicht zutreffend", "Nicht zutreffend"]]

    choices = ['positive', 'emotional']


    tweets = get_tweets("html994_selected_tweets_for_labeling.csv")

    # Treatments as list of list.
    treatment_cycles = []
    tweet_cycles = []
    for i in range(num_participants):
        # Makes personalized random cycle of tweets
        shuffled_tweets = random.sample(tweets, len(tweets))
        # Turns tweets into cycles and stores them in a list.
        tweet_cycle = itertools.cycle(shuffled_tweets)
        tweet_cycles.append(tweet_cycle)


class Subsession(BaseSubsession):
    def creating_session(self):
        count = 0
        for p in self.get_players():
            choices = random.sample(Constants.choices, len(Constants.choices))
            p.choice1 = choices[0]
            p.choice2 = choices[1]
            p.tweet = next(Constants.tweet_cycles[count])
            count += 1

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    feedback = models.StringField(blank=True)
    tweet = models.StringField()
    choice1 = models.StringField()
    choice2 = models.StringField()
    pos_rating = make_field(Constants.positive)
    emo_rating = make_field(Constants.emotional)
