import pandas as pd
sd = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(sd.groupby('Primary Fur Color').count())