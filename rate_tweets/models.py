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


class Subsession(BaseSubsession):
    def get_tweets(self):
        import csv

        with open('data/example_corona_tweets.tsv', newline='') as f:
           reader = csv.reader(f)
           data = list(reader)


           self.session.vars['data'] = set(map(str, data))

    def set_sample(self):
        sample = set()
        for i in range(Constants.q_per_round):
            try:
                sample.add(self.session.vars['data'].pop())
            except KeyError:
                print('no more tweets')
                break

        index = range(len(sample))

        return dict(zip(index, sample))

    def set_choices_cycle(self, start_at):

       choice_1 =[["Negativ","Negativ"],["Neutral","Neutral"],["Positiv","Positiv"]]
       choice_2 = [["Pessimistisch","Pessimistisch"],["Neutral","Neutral"],["Optimistisch","Optimistisch"]]
       choice_3 = [["Verärgert","Verärgert"],["Neutral","Neutral"],["Zufrieden","Zufrieden"]]
       choice_4 = [["Sachlich","Sachlich"],["Neutral","Neutral"],["Emotional","Emotional"]]
       choices = [choice_1, choice_2, choice_3, choice_4]
       choices_cycle = it.cycle(choices)

       return it.islice(choices_cycle, 0, None)



    def creating_session(self):
        self.get_tweets()
        count = 0
        for p in self.get_players():

            #p.sample = self.set_sample()
            p.participant.vars['sample'] = self.set_sample()
            p.participant.vars['counter'] = 0
            p.participant.vars['choices'] = self.set_choices_cycle(count)
            p.participant.vars['rating'] = models.StringField(widget= widgets.RadioSelectHorizontal, label='',choices =next(p.participant.vars['choices']))

            count += 1
class Group(BaseGroup):
    pass


class Player(BasePlayer):

    
    rating1 = models.StringField(widget= widgets.RadioSelectHorizontal, label='',choices =[["Pessimistisch","Pessimistisch"],["Neutral","Neutral"],["Optimistisch","Optimistisch"]])


#    def choices():
#        import random

#        return
#choices()


    #rating = models.StringField(widget= widgets.RadioSelectHorizontal, choices=[["Negativ","Negativ"],["Neutral","Neutral"],["Positiv","Positiv"]])
