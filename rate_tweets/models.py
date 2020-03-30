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

<<<<<<< Updated upstream

=======
def make_field(choice):
    return models.StringField(
        choices=choice,
        label="",
        widget=widgets.RadioSelectHorizontal,
    )



    with open('data/test_data.csv', newline='') as f:
       reader = pd.read_csv(f)
       urls = reader.tweet_url.tolist()
       urls[-1]
       reader
def get_tweets():
    import time
    with open('data/test_data.csv', newline='') as f:
       reader = pd.read_csv(f)
       urls = reader.tweet_url.head(21).tolist()
       # tweets = []
       # for tweet in urls:
       #     tweets.append(get_embed_tweet('https://twitter.com' + tweet))
       #     time.sleep(0.2)  #wait to not get banned
       #     print ('one more')
       #
       # print(tweets[0])
       return set(urls)
>>>>>>> Stashed changes

class Constants(BaseConstants):
    name_in_url = 'rate_tweets'
    players_per_group = None
    num_rounds = 10
    q_per_round = 10



    def get_tweets():
        import csv

        with open('data/example_corona_tweets.tsv', newline='') as f:
           reader = csv.reader(f)
           data = list(reader)


           return set(map(tuple, data))


    tweets = get_tweets()
class Subsession(BaseSubsession):


    def set_sample(self):
        sample = 'placeholder'

        try:
            #sample.add(Constants.tweets.pop()[0])
            sample = Constants.tweets.pop()[0]
            print(sample)
        except KeyError:
            print('no more tweets')


        #index = range(len(sample))

        return str(sample) #dict(zip(index, sample))



    def creating_session(self):

        for p in self.get_players():

            #p.sample = self.set_sample()
            p.tweet = self.set_sample()

class Group(BaseGroup):
    pass


class Player(BasePlayer):

    tweet = models.StringField()
    rating = models.StringField(widget= widgets.RadioSelectHorizontal, label='',choices =[["Pessimistisch","Pessimistisch"],["Neutral","Neutral"],["Optimistisch","Optimistisch"]])


#    def choices():
#        import random

#        return
#choices()


    #rating = models.StringField(widget= widgets.RadioSelectHorizontal, choices=[["Negativ","Negativ"],["Neutral","Neutral"],["Positiv","Positiv"]])
