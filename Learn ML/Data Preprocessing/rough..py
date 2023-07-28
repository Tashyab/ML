#Importing libraries
import pandas as pd
from sklearn.datasets import load_iris

#Iris dataset
ds = load_iris()

#Features and Dependent variables
print(ds.data)
print(ds.target)