import numpy as np
import pandas as pd
#import sklearn
#import tensorflow as tf


data = pd.read_csv("student-mat.csv", sep=";")

data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]
#print(data.head())

predict = "G1"#, "G2", "G3"



x = np.array(data.drop([predict], 1))
y = np.array(data[predict])


