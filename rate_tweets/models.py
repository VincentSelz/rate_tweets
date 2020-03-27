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


author = 'Your name here'

doc = """
Your app description
"""



class Constants(BaseConstants):
    name_in_url = 'rate_tweets'
    players_per_group = None
    num_rounds = 10
    q_per_round = 10
    self.get_tweets()

class Subsession(BaseSubsession):
    def get_tweets(self):
        import csv

        with open('data/example_corona_tweets.tsv', newline='') as f:
           reader = csv.reader(f)
           data = list(reader)


           self.session.vars['data'] = set(map(tuple, data))

    def set_sample(self):
        sample = set()

        try:
            sample.add(self.session.vars['data'].pop()[0])
        except KeyError:
            print('no more tweets')


        index = range(len(sample))

        return dict(zip(index, sample))



    def creating_session(self):

        count = 0
        for p in self.get_players():

            #p.sample = self.set_sample()
            p.participant.vars['sample'] = self.set_sample()

class Group(BaseGroup):
    pass


class Player(BasePlayer):


    rating = models.StringField(widget= widgets.RadioSelectHorizontal, label='',choices =[["Pessimistisch","Pessimistisch"],["Neutral","Neutral"],["Optimistisch","Optimistisch"]])


#    def choices():
#        import random

#        return
#choices()


    #rating = models.StringField(widget= widgets.RadioSelectHorizontal, choices=[["Negativ","Negativ"],["Neutral","Neutral"],["Positiv","Positiv"]])
