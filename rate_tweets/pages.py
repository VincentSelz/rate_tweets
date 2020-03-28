from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1


class MyPage(Page):
    #def vars_for_template(self):
    #    tweets = self.participant.vars['sample'][0]
    #    print('Tweet is displayed')
    #    return dict(
    #        currentTweet= tweets,)
    form_model = 'player'
    def get_form_fields(self):
        if self.participant.vars['treatment'] == 'positive':
            form_fields = ['pos_rating']
            return form_fields
        elif self.participant.vars['treatment'] == 'optimistic':
            form_fields = ['opt_rating']
            return form_fields
        elif self.participant.vars['treatment'] == 'happiness':
            form_fields = ['hap_rating']
            return form_fields
        elif self.participant.vars['treatment'] == 'emotional':
            form_fields = ['emo_rating']
            return form_fields

    #form_fields = ['rating']





class ExitPage(Page):
    def is_displayed(self):
        return self.round_number > 10


page_sequence = [Introduction, MyPage, ExitPage
        ]
