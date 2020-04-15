"""Quick preliminary data exploration."""
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np
import seaborn as sns

# Read in data
with open('survey_data/scale_after_scale_2020-04-15.csv', newline='') as f:
    reader = pd.read_csv(f)
    
# Drop unncecessary columns    
columns = list(reader.columns)
del columns[20:24]
df = reader.drop(columns, axis=1)

# Drop empty rows 
df.dropna(how='all', inplace=True)   

# Rename columns 
df.columns = ['pos', 'opt', 'hap','emo']

# Recode the values
values = [-1, 0, 1, np.nan]
value_dict = {'pos': values, 'opt':values, 'hap':values, 'emo': [-1, 1, np.nan]}
to_replace = {'pos': ['Negativ','Neutral','Positiv', 'Nicht zutreffend'], 'opt': ['Pessimistisch', 'Neutral', 'Optimistisch', 'Nicht zutreffend'], 'hap': ['Verärgert', 'Neutral', 'Zufrieden', 'Nicht zutreffend'], 'emo': ['Emotional', 'Sachlich', 'Nicht zutreffend' ]}
df = df.replace(to_replace=to_replace, value=value_dict)

# Get first correlation matrix with spearman
corr_matrix = df.corr(method='spearman')

# Beware that NaN values are kicked out. Hence, we cannot say something about the relationship of Nicht zutreffend and the other values.

# Make heatmap
plt.figure(figsize=(20, 16))

sns.heatmap(
    data=df.corr(method="spearman"),
    center=0,
    annot=True,
    linecolor="white",
    linewidth=0.1,
    cmap="coolwarm",
)

plt.title("Heatmap of Correlation Matrix of Scales", fontsize=20)

# Export it to screenshots
plt.savefig("screenshots/heatmap.png")