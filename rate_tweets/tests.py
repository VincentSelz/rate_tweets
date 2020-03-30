from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):
    def play_round(self):
        if self.round_number ==1:
            yield pages.Introduction
        if self.player.treatment == 'positive':
            yield pages.MyPage, dict(pos_rating="Positiv")
        if self.player.treatment == 'emotional':
            yield pages.MyPage, dict(emo_rating="Emotional")
        if self.player.treatment == 'happiness':
            yield pages.MyPage, dict(hap_rating="Zufrieden")
        if self.player.treatment == 'optimistic':
            yield pages.MyPage, dict(opt_rating="Neutral")
        if self.round_number == 10 or self.round_number == 20 or self.round_number == 30:
            yield pages.ExitPage
