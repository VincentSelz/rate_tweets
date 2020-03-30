from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1


def get_embed_tweet(url):
    '''returns embeded html as String'''
    # importing the requests library
    import requests

    # api-endpoint
    URL = "https://publish.twitter.com/oembed"#"?buttonType=HashtagButton&query=asdfasdf&widget=Button"

    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'url': url,
        'buttonType': 'HashtagButton',
        'hide_thread': 'false'}

    # sending get request and saving the response as response object
    r = requests.get(url = URL, params = PARAMS)

    # extracting data in json format
    data = r.json()

    return data['html']


class MyPage(Page):
<<<<<<< Updated upstream
    # def vars_for_template(self):
    #     tweets = self.participant.vars['sample']
    #     print('asdfasdfasdf')
    #     return dict(
    #         currentTweet= tweets,)
=======
    def vars_for_template(self):
       tweets = get_embed_tweet('https://twitter.com' + self.player.tweet)
       print('Tweet is displayed')
       return dict(
           currentTweet= tweets,)
>>>>>>> Stashed changes

    form_model = 'player'

    form_fields = ['rating']





class ExitPage(Page):
    def is_displayed(self):
        return self.round_number > 10


page_sequence = [Introduction, MyPage, ExitPage
        ]
