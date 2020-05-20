import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import style
import seaborn as sns 
df1=pd.read_csv('sentiment.csv',header=0,encoding = 'unicode_escape')

positive=0
negative=0
neutral=0
for tweet in df1.iterrows():
    if tweet[1][1]=='Positive':
        positive+=1
    if tweet[1][1]=='Neutral':
        neutral+=1
    if tweet[1][1]=='Negative':
        negative+=1
labels = 'Positive', 'Negative', 'Neutral'
sizes = [positive, negative,neutral]
colors = ['yellow', 'red', 'lightblue']
explode = (0, 0, 0)  # explode 1st slice

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()
