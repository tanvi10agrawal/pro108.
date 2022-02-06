import csv
import plotly.figure_factory as ff
import pandas as pd

df=pd.read_csv("data.csv")

graph=ff.create_distplot([df["AvgRating"].tolist()],["AvgRating"])
graph.show()