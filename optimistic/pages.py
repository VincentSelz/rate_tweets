from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1

class MyPage(Page):
    form_model = 'player'
    form_fields = ['rating']

class ExitPage(Page):
    def is_displayed(self):
        return self.round_number == 10


page_sequence = [MyPage, ExitPage
        ]
