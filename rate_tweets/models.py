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


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'rate_tweets'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    rating = models.StringField(widget= widgets.RadioSelectHorizontal, label="",choices =[["Negativ","Negativ"],["Neutral","Neutral"],["Positiv","Positiv"]])
#    def choices():
#        import random
#        choice_1 =[["Negativ","Negativ"],["Neutral","Neutral"],["Positiv","Positiv"]]
#        choice_2 = [["Pessimistisch","Pessimistisch"],["Neutral","Neutral"],["Optimistisch","Optimistisch"]]
#        choice_3 = [["Verärgert","Verärgert"],["Neutral","Neutral"],["Zufrieden","Zufrieden"]]
#        choice_4 = [["Sachlich","Sachlich"],["Neutral","Neutral"],["Emotional","Emotional"]]
#        x = str(random.randrange(1,4))
#        return
#choices()


    #rating = models.StringField(widget= widgets.RadioSelectHorizontal, choices=[["Negativ","Negativ"],["Neutral","Neutral"],["Positiv","Positiv"]])
