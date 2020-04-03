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
       tweets = reader['player.tweet'].tolist()
       return tweets

def cycle_tweets(list):
    tweet_cycles = []
    for i in range(10):
        try:
            shuffled_tweets = random.sample(list, len(list))
            print('list is shuffled for player {}'.format(i))
            # Turns treatment into cycles and stores them in a list.
            tweet_cycle = itertools.cycle(shuffled_tweets)
            tweet_cycles.append(tweet_cycle)
        except ValueError:
            print("Passed in list is empty.")
    return tweet_cycles


class Constants(BaseConstants):
    name_in_url = 'curated_rate_tweets'
    players_per_group = None
    num_participants = 10
    num_rounds = 40

    #Choices for different StringFields
    positive =[["Negativ","Negativ"],["Neutral","Neutral"],["Positiv","Positiv"],["Nicht zutreffend", "Nicht zutreffend"]]
    optimistic = [["Pessimistisch","Pessimistisch"],["Neutral","Neutral"],["Optimistisch","Optimistisch"],["Nicht zutreffend", "Nicht zutreffend"]]
    happiness = [["Verärgert","Verärgert"],["Neutral","Neutral"],["Zufrieden","Zufrieden"],["Nicht zutreffend", "Nicht zutreffend"]]
    emotional = [["Sachlich","Sachlich"],["Emotional","Emotional"],["Nicht zutreffend", "Nicht zutreffend"]]
    choices = [['positive'], ['optimistic'], ['happiness'], ['emotional']]

    pos_set = get_tweets("pos_set_html.csv")
    hap_set = get_tweets("hap_set_html.csv")
    opt_set = get_tweets("opt_set_html.csv")
    emo_set = get_tweets("emo_set_html.csv")

    pos_cycles = cycle_tweets(pos_set)
    hap_cycles = cycle_tweets(hap_set)
    opt_cycles = cycle_tweets(opt_set)
    emo_cycles = cycle_tweets(emo_set)

    # Treatments as list of list.
    treatment_cycles = []
    for i in range(num_participants):
        shuffled_rating = random.sample(choices, len(choices))
        #Expands treatments to 10 rounds per treatment.
        real_treatments = extend_treatment(shuffled_rating)
        # Turns treatment into cycles and stores them in a list.
        treatment_cycle = itertools.cycle(real_treatments)
        treatment_cycles.append(treatment_cycle)

class Subsession(BaseSubsession):
    def creating_session(self):
        count = 0
        for p in self.get_players():
            p.treatment = next(Constants.treatment_cycles[count])
            if p.treatment == "positive":
                try:
                    p.tweet = next(Constants.pos_cycles[count])
                except StopIteration:
                    print("No tweets could be found.")
                    continue
            elif p.treatment == "happiness":
                try:
                    p.tweet = next(Constants.hap_cycles[count])
                except StopIteration:
                    print("No tweets could be found.")
                    continue
            elif p.treatment == "emotional":
                try:
                    p.tweet = next(Constants.emo_cycles[count])
                except StopIteration:
                    print("No tweets could be found.")
                    continue
            elif p.treatment == "optimistic":
                try:
                    p.tweet = next(Constants.opt_cycles[count])
                except StopIteration:
                    print("No tweets could be found.")
                    continue
            count += 1

class Group(BaseGroup):
    pass


class Player(BasePlayer):

    # Set tweet fields
    tweet = models.StringField()
    treatment = models.StringField()

    # Set rating fields
    pos_rating = make_field(Constants.positive)
    opt_rating = make_field(Constants.optimistic)
    hap_rating = make_field(Constants.happiness)
    emo_rating = make_field(Constants.emotional)
