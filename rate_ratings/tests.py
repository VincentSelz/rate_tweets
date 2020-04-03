from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants

import random


class PlayerBot(Bot):
    def play_round(self):
        if self.round_number ==1:
            yield pages.Introduction
        yield pages.MyPage, random.choice([dict(
                            pos_scale="Negativ/Positiv",
                            emo_scale="",
                            hap_scale="",
                            opt_scale="Pessimistisch/Optimistisch",
                            not_applicable=""
                            ),
                            dict(
                            pos_scale='',
                            emo_scale='',
                            hap_scale='',
                            opt_scale='',
                            not_applicable="Nicht zutreffend"
                            ),
                            dict(
                            pos_scale="Negativ/Positiv",
                            emo_scale='',
                            hap_scale='',
                            opt_scale='',
                            not_applicable='',
                            ),
                            dict(
                            pos_scale='',
                            emo_scale='',
                            hap_scale="Verärgert/Zufrieden",
                            opt_scale='',
                            not_applicable='',
                            )]
                            )
        if self.round_number == 10 or self.round_number == 20 or self.round_number == 30:
            yield pages.ExitPage
