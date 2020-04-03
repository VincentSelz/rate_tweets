
import pandas as pd

with open('out_data/rate_ratings.csv', newline='') as f:
    reader = pd.read_csv(f)
scales = {"pos_set": "pos_scale", "hap_set":"hap_scale", "emo_set": "emo_scale", "opt_set": "opt_scale"}

for set in scales:
    scales[set] = reader.dropna(subset=["player.{}".format(scales[set])])
    scales[set] = scales[set].drop(scales[set].columns.difference(['player.tweet', '{}'.format(scales[set])]), axis=1)
    scales[set].to_csv('data/'+str(set)+'_html.csv', index=False)
