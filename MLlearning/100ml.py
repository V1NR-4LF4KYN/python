import pandas as pd
import numpy as np
from sklearn.preprocessing import Imputer

dataset = pd.read_csv('Data.csv')
x = dataset.iloc[:  , :-1].values
y = dataset.iloc[:, 3].values

