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
    name_in_url = 'rate_tweets'
    players_per_group = None
    num_rounds = 10
    q_per_round = 10
    positive =[["Negativ","Negativ"],["Neutral","Neutral"],["Positiv","Positiv"]]
    optimistic = [["Pessimistisch","Pessimistisch"],["Neutral","Neutral"],["Optimistisch","Optimistisch"]]
    happiness = [["Verärgert","Verärgert"],["Neutral","Neutral"],["Zufrieden","Zufrieden"]]
    emotional = [["Sachlich","Sachlich"],["Neutral","Neutral"],["Emotional","Emotional"]]
    choices = ['positive', 'optimistic', 'happiness', 'emotional']
    def get_tweets():
        with open('data/example_corona_tweets.tsv', newline='') as f:
           reader = csv.reader(f)
           data = list(reader)
        return set(map(tuple, data))
    tweets = get_tweets()

class Subsession(BaseSubsession):
    def set_sample(self):
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
        return str(sample)

    def creating_session(self):
        shuffled_ratings = random.sample(Constants.choices, len(Constants.choices))
        treatments = itertools.cycle(shuffled_ratings)
        print('Shuffle ratings')
        for p in self.get_players():
            p.treatment = next(treatments)
            p.participant.vars['treatment'] = p.treatment
            p.tweet = self.set_sample()

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
