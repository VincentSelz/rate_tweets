"""Quick preliminary data exploration."""
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np
import seaborn as sns

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
two_scales = drop_stuff(reader('two_scales_2020-04-27.csv'))



result = pd.concat([all_scales, two_scales], join='outer', sort=False)

# Get first correlation matrix with spearman
corr_matrix = df.corr(method='spearman')

# Beware that NaN values are kicked out. Hence, we cannot say something about the relationship of Nicht zutreffend and the other values.

# Make heatmap
plt.figure(figsize=(25, 20))

sns.heatmap(
    data=df.corr(method="spearman"),
    center=0,
    annot=True,
    linecolor="white",
    linewidth=0.1,
    cmap="coolwarm",
)

plt.title("Heatmap of Correlation Matrix of Scales", fontsize=30)

# Export it to screenshots
plt.savefig("screenshots/heatmap.png")