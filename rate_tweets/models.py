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
    positive =[["Negativ","Negativ"],["Neutral","Neutral"],["Positiv","Positiv"]]
    optimistic = [["Pessimistisch","Pessimistisch"],["Neutral","Neutral"],["Optimistisch","Optimistisch"]]
    happiness = [["Verärgert","Verärgert"],["Neutral","Neutral"],["Zufrieden","Zufrieden"]]
    emotional = [["Sachlich","Sachlich"],["Neutral","Neutral"],["Emotional","Emotional"]]
    choices = [positive,optimistic,happiness,emotional]
    rating_1 = make_field(positive)
    rating_2 = make_field(optimistic)
    rating_3 = make_field(happiness)
    rating_4 = make_field(emotional)
    ratings = [rating_1,rating_2,rating_3,rating_4]


class Subsession(BaseSubsession):
    #def creating_session(self):
    #    import itertools
    #    import random
    #    sub_ratings = Constants.ratings.copy()
    #    if self.round_number == 1:
    #        sub_rating = random.shuffle(sub_ratings)
    #    rating = itertools.cycle(sub_rating)
    #    for p in self.get_players():
    #        p.player.vars['rating'] = next(rating)
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    #def example(self):
    #    rating = self.player.vars['rating']
    #    return rating
    rating = make_field([["Negativ","Negativ"],["Neutral","Neutral"],["Positiv","Positiv"]])
