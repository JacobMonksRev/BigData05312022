# Pandas documentation: https://pandas.pydata.org/docs/

import pandas as pd
import matplotlib.pyplot as plt

temp_df = pd.read_csv('example.csv')    # creates a dataframe using a csv file
temp_df.plot()                          # turns the dataframe into a plotted graph
# set subplots=True if you want to see each column graphed individually:
# temp_df.plot(subplots=True)
plt.show()                              # shows the graph