import pandas as pd

import plotly.express as px

#reading data from csv files
df = pd.read_csv("data.csv")
fig = px.bar(df, x='InternetUsers', y='Country')
fig.show()
