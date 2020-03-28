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
    name_in_url = 'positive'
    players_per_group = None
    num_rounds = 10
    positive =[["Negativ","Negativ"],["Neutral","Neutral"],["Positiv","Positiv"]]
    optimistic = [["Pessimistisch","Pessimistisch"],["Neutral","Neutral"],["Optimistisch","Optimistisch"]]
    happiness = [["Verärgert","Verärgert"],["Neutral","Neutral"],["Zufrieden","Zufrieden"]]
    emotional = [["Sachlich","Sachlich"],["Neutral","Neutral"],["Emotional","Emotional"]]
    choices = [positive,optimistic,happiness,emotional]
    def get_tweets():
        with open('data/example_corona_tweets.tsv', newline='') as f:
           reader = csv.reader(f)
           data = list(reader)

        return set(map(tuple, data))
    tweets = get_tweets()


class Subsession(BaseSubsession):
    def set_sample(self):
        #sample = set()
        sample = ''
        try:
            #sample.add(Constants.tweets.pop()[0])
            sample = Constants.tweets.pop()[0]
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
    rating = make_field(Constants.positive)
