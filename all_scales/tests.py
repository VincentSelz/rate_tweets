from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants

import random


class PlayerBot(Bot):
    def play_round(self):
        if self.round_number ==1:
            yield pages.Introduction
        yield pages.MyPage, dict(
                            pos_rating=random.choice(["Negativ","Neutral","Positiv","Nicht zutreffend"]),
                            emo_rating=random.choice(["Emotional", "Sachlich", "Nicht zutreffend"]),
                            hap_rating=random.choice(["Zufrieden", "Verärgert", "Neutral", "Nicht zutreffend"]),
                            opt_rating=random.choice(["Pessimistisch","Neutral", "Optimistisch", "Nicht zutreffend"])
                            )
        if self.round_number == 10 or self.round_number == 20 or self.round_number == 30:
            yield pages.ExitPage
