from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    pass

class MyPage(Page):
    form_model = 'player'
    form_fields = ['rating']


page_sequence = [Introduction, MyPage]
