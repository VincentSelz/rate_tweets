from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1


class MyPage(Page):
    form_model = 'player'
    form_fields = ['pos_rating','opt_rating','hap_rating','emo_rating']


class ExitPage(Page):
    def is_displayed(self):
        return self.round_number == 10 or self.round_number == 20 or self.round_number == 30


page_sequence = [Introduction, MyPage, ExitPage]
