from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

SESSION_CONFIGS = [
    dict(
        name='rate_tweets',
        num_demo_participants=4,
        app_sequence=['rate_tweets'],
        num_demo_rounds=40,
    ),
    dict(
        name='rate_tweets_with_bots',
        num_demo_participants=4,
        app_sequence=['rate_tweets'],
        num_demo_rounds=40,
        use_browser_bots=True,
    ),
    dict(
        name='all_scales',
        num_demo_participants=4,
        app_sequence=['all_scales'],
        num_demo_rounds=40,
    ),
    dict(
        name='all_scales_with_bots',
        num_demo_participants=4,
        app_sequence=['all_scales'],
        num_demo_rounds=40,
        use_browser_bots=True,
    ),
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'u&oe58surw@yd^jktu7&_hc!g=&@gfz6-*n%9ab)(j2y26a6+l'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
