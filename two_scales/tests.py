from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants

import random


class PlayerBot(Bot):
    def play_round(self):
        if self.round_number ==1:
            yield pages.Introduction
        if self.player.choice1 == 'positive':
            yield pages.MyPage1, dict(pos_rating=random.choice(["Negativ","Neutral","Positiv","Nicht zutreffend"]))
        if self.player.choice1 == 'emotional':
            yield pages.MyPage1, dict(emo_rating=random.choice(["Emotional", "Sachlich", "Nicht zutreffend"]))
        if self.player.choice2 == 'positive':
            yield pages.MyPage2, dict(pos_rating=random.choice(["Negativ","Neutral","Positiv","Nicht zutreffend"]))
        if self.player.choice2 == 'emotional':
            yield pages.MyPage2, dict(emo_rating=random.choice(["Emotional", "Sachlich", "Nicht zutreffend"]))
        if self.round_number == 10 or self.round_number == 20 or self.round_number == 30 or self.round_number == 40:
            yield pages.ExitPage
