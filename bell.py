import pandas as pd
import csv
import plotly.figure_factory as ff
df=pd.read_csv("data")
chart=ff.create_distplot([df["Mobile Brand"].tolist()], ["Avg Rating"])
chart.show()