#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 20:24:03 2020

@author: vincentselz
"""

"""Quick preliminary data exploration."""

import pandas as pd
import numpy as np

def reader(csv):
    """Read in data from folder survey_data."""
    with open('survey_data/'+str(csv), newline='') as f:
        reader = pd.read_csv(f)
    return reader

def drop_stuff(reader):
    """Filter out unnecessary columns, drop empy rows and ename the columns."""
    df = reader.filter(['player.tweet', 'player.pos_rating','player.emo_rating'])
    df.dropna(how='all', subset=['player.pos_rating','player.emo_rating'], inplace=True)
    df.columns = ['tweet', 'pos', 'emo']
    return df

def recode_values(df):
    """Recode the values in the dataframe."""
    value_dict = {'pos': [-1, 0, 1, np.nan],
                  'emo': [-1, 1, np.nan]
                  }
    to_replace = {'pos': ['Negativ','Neutral','Positiv', 'Nicht zutreffend'],
                  'emo': ['Emotional', 'Sachlich', 'Nicht zutreffend']
                  }
    return df.replace(to_replace=to_replace, value=value_dict, inplace=True)

all_scales = drop_stuff(reader('scale_after_scale_2020-04-17.csv'))
two_scales = drop_stuff(reader('two_scales_2020-04-28.csv'))



result = pd.concat([all_scales, two_scales], join='outer', sort=False)

unique_tweets = result.drop_duplicates(subset='tweet')

assert result['tweet'].nunique() == len(unique_tweets)

# This is done to verify that we are now working with a subset of the orginal tweets.
with open('data/html994_selected_tweets_for_labeling.csv', newline='') as f:
    og_list = pd.read_csv(f)

# Clean up the html
unique_list = unique_tweets.tweet.str.wrap(10,replace_whitespace=True).to_list()
big_list = og_list['0'].str.wrap(10,replace_whitespace=True).to_list()

# Transform into set
unique_set = set(unique_list)
big_set = set(big_list)
diff = unique_set.intersection(big_set)

if unique_set.issubset(big_set) == True and len(diff) == len(unique_tweets):
    unique_tweets.to_csv('data/unique_tweets.csv', index=False)
else:
    print("Unique tweets are not a subset the original list.")
