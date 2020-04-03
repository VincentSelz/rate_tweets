from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants

import random


class PlayerBot(Bot):
    def play_round(self):
        if self.round_number ==1:
            yield pages.Introduction
        if self.player.treatment == 'positive':
            yield pages.MyPage, dict(pos_rating=random.choice(["Negativ","Neutral","Positiv","Nicht zutreffend"]))
        if self.player.treatment == 'emotional':
            yield pages.MyPage, dict(emo_rating=random.choice(["Emotional", "Sachlich", "Nicht zutreffend"]))
        if self.player.treatment == 'happiness':
            yield pages.MyPage, dict(hap_rating=random.choice(["Zufrieden", "Neutral", "Verärgert", "Nicht zutreffend"]))
        if self.player.treatment == 'optimistic':
            yield pages.MyPage, dict(opt_rating=random.choice(["Pessimistisch","Neutral", "Optimistisch", "Nicht zutreffend"]))
        if self.round_number == 10 or self.round_number == 20 or self.round_number == 30:
            yield pages.ExitPage
