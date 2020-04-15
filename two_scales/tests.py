from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants

import random


class PlayerBot(Bot):
    def play_round(self):
        if self.round_number ==1:
            yield pages.Introduction
        if self.round_number ==1:
            yield pages.GIF
        if self.player.choice1 == 'positive':
            yield pages.MyPage1, dict(pos_rating=random.choice(["Negativ","Neutral","Positiv","Nicht zutreffend"]))
        if self.player.choice1 == 'emotional':
            yield pages.MyPage1, dict(emo_rating=random.choice(["Emotional", "Sachlich", "Nicht zutreffend"]))
        if self.player.choice1 == 'happiness':
            yield pages.MyPage1, dict(hap_rating=random.choice(["Zufrieden", "Neutral", "Verärgert", "Nicht zutreffend"]))
        if self.player.choice1 == 'optimistic':
            yield pages.MyPage1, dict(opt_rating=random.choice(["Pessimistisch","Neutral", "Optimistisch", "Nicht zutreffend"]))
        if self.player.choice2 == 'positive':
            yield pages.MyPage2, dict(pos_rating=random.choice(["Negativ","Neutral","Positiv","Nicht zutreffend"]))
        if self.player.choice2 == 'emotional':
            yield pages.MyPage2, dict(emo_rating=random.choice(["Emotional", "Sachlich", "Nicht zutreffend"]))
        if self.player.choice2 == 'happiness':
            yield pages.MyPage2, dict(hap_rating=random.choice(["Zufrieden", "Neutral", "Verärgert", "Nicht zutreffend"]))
        if self.player.choice2 == 'optimistic':
            yield pages.MyPage2, dict(opt_rating=random.choice(["Pessimistisch","Neutral", "Optimistisch", "Nicht zutreffend"]))
        if self.player.choice3 == 'positive':
            yield pages.MyPage3, dict(pos_rating=random.choice(["Negativ","Neutral","Positiv","Nicht zutreffend"]))
        if self.player.choice3 == 'emotional':
            yield pages.MyPage3, dict(emo_rating=random.choice(["Emotional", "Sachlich", "Nicht zutreffend"]))
        if self.player.choice3 == 'happiness':
            yield pages.MyPage3, dict(hap_rating=random.choice(["Zufrieden", "Neutral", "Verärgert", "Nicht zutreffend"]))
        if self.player.choice3 == 'optimistic':
            yield pages.MyPage3, dict(opt_rating=random.choice(["Pessimistisch","Neutral", "Optimistisch", "Nicht zutreffend"]))
        if self.player.choice4 == 'positive':
            yield pages.MyPage4, dict(pos_rating=random.choice(["Negativ","Neutral","Positiv","Nicht zutreffend"]))
        if self.player.choice4 == 'emotional':
            yield pages.MyPage4, dict(emo_rating=random.choice(["Emotional", "Sachlich", "Nicht zutreffend"]))
        if self.player.choice4 == 'happiness':
            yield pages.MyPage4, dict(hap_rating=random.choice(["Zufrieden", "Neutral", "Verärgert", "Nicht zutreffend"]))
        if self.player.choice4 == 'optimistic':
            yield pages.MyPage4, dict(opt_rating=random.choice(["Pessimistisch","Neutral", "Optimistisch", "Nicht zutreffend"]))
        if self.round_number == 10 or self.round_number == 20 or self.round_number == 30:
            yield pages.ExitPage
