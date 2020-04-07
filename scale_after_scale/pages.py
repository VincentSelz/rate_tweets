from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1

class GIF(Page):
    def is_displayed(self):
        return self.round_number == 1

class MyPage1(Page):
    form_model = 'player'
    def get_form_fields(self):
        if self.player.choice1 == 'positive':
            form_fields = ['pos_rating','feedback']
        elif self.player.choice1 == 'optimistic':
            form_fields = ['opt_rating','feedback']
        elif self.player.choice1 == 'happiness':
            form_fields = ['hap_rating','feedback']
        elif self.player.choice1 == 'emotional':
            form_fields = ['emo_rating','feedback']
        return form_fields

class MyPage2(Page):
    form_model = 'player'
    def get_form_fields(self):
        if self.player.choice2 == 'positive':
            form_fields = ['pos_rating','feedback']
        elif self.player.choice2 == 'optimistic':
            form_fields = ['opt_rating','feedback']
        elif self.player.choice2 == 'happiness':
            form_fields = ['hap_rating','feedback']
        elif self.player.choice2 == 'emotional':
            form_fields = ['emo_rating','feedback']
        return form_fields

class MyPage3(Page):
    form_model = 'player'
    def get_form_fields(self):
        if self.player.choice3 == 'positive':
            form_fields = ['pos_rating','feedback']
        elif self.player.choice3 == 'optimistic':
            form_fields = ['opt_rating','feedback']
        elif self.player.choice3 == 'happiness':
            form_fields = ['hap_rating','feedback']
        elif self.player.choice3 == 'emotional':
            form_fields = ['emo_rating','feedback']
        return form_fields

class MyPage4(Page):
    form_model = 'player'
    def get_form_fields(self):
        if self.player.choice4 == 'positive':
            form_fields = ['pos_rating','feedback']
        elif self.player.choice4 == 'optimistic':
            form_fields = ['opt_rating','feedback']
        elif self.player.choice4 == 'happiness':
            form_fields = ['hap_rating','feedback']
        elif self.player.choice4 == 'emotional':
            form_fields = ['emo_rating','feedback']
        return form_fields

class ExitPage(Page):
    def is_displayed(self):
        return self.round_number == 10 or self.round_number == 20 or self.round_number == 30


page_sequence = [Introduction, GIF, MyPage1, MyPage2, MyPage3, MyPage4, ExitPage]
