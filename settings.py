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
        name='scale_after_scale',
        num_demo_participants=4,
        app_sequence=['scale_after_scale'],
        num_demo_rounds=40,
    ),
    dict(
        name='scale_after_scale_bot',
        num_demo_participants=4,
        app_sequence=['scale_after_scale'],
        num_demo_rounds=40,
        use_browser_bots=True
    ),
    dict(
        name='scale_after_scale_down',
        num_demo_participants=4,
        app_sequence=['scale_after_scale_down'],
        num_demo_rounds=40,
    ),
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'de'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    dict(
        name='tweet_survey_scale_up_demo',
        display_name='Tweet Survey Demo Scale Up',
        # without label there is only one url (no prob since everybody can play as often as they want)
        #participant_label_file='_rooms/tweet_survey.txt',
        #use_secure_urls=True #adds an hash to the url
    ),
    dict(
        name='tweet_survey_scale_down_demo',
        display_name='Tweet Survey Demo Scale Down',
        # without label there is only one url (no prob since everybody can play as often as they want)
        #participant_label_file='_rooms/tweet_survey.txt',
        #use_secure_urls=True #adds an hash to the url
    )]

# AUTH_LEVEL:
# this setting controls which parts of your site are freely accessible,
# and which are password protected:
# - If it's not set (the default), then the whole site is freely accessible.
# - If you are launching a study and want visitors to only be able to
#   play your app if you provided them with a start link, set it to STUDY.
# - If you would like to put your site online in public demo mode where
#   anybody can play a demo version of your game, but not access the rest
#   of the admin interface, set it to DEMO.

# for flexibility, you can set it in the environment variable OTREE_AUTH_LEVEL
AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'u&oe58surw@yd^jktu7&_hc!g=&@gfz6-*n%9ab)(j2y26a6+l'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
