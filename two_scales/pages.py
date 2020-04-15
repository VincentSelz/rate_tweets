from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1

class MyPage1(Page):
    form_model = 'player'
    def get_form_fields(self):
        if self.player.choice1 == 'positive':
            form_fields = ['pos_rating','feedback']
        elif self.player.choice1 == 'emotional':
            form_fields = ['emo_rating','feedback']
        return form_fields

class MyPage2(Page):
    form_model = 'player'
    def get_form_fields(self):
        if self.player.choice2 == 'positive':
            form_fields = ['pos_rating','feedback']
        elif self.player.choice2 == 'emotional':
            form_fields = ['emo_rating','feedback']
        return form_fields

class ExitPage(Page):
    def is_displayed(self):
        return self.round_number == 10 or self.round_number == 20 or self.round_number == 30 


page_sequence = [Introduction, MyPage1, MyPage2, ExitPage]
