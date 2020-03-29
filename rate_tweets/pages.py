from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1


class MyPage(Page):
    form_model = 'player'
    def get_form_fields(self):
        if self.player.treatment == 'positive':
            form_fields = ['pos_rating']
        elif self.player.treatment == 'optimistic':
            form_fields = ['opt_rating']
        elif self.player.treatment == 'happiness':
            form_fields = ['hap_rating']
        elif self.player.treatment == 'emotional':
            form_fields = ['emo_rating']
        return form_fields

class ExitPage(Page):
    def is_displayed(self):
        return self.round_number == 10 or self.round_number == 20 or self.round_number == 30


page_sequence = [Introduction, MyPage, ExitPage]
