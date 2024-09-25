import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

import matplotlib.pyplot as plt
import seaborn as sns

import pickle
import json

df = pd.read_csv('medical_insurance.csv')
print(df)

df.isna().sum()
df['gender'].replace({'male': 1, 'female': 0, 'MALE': 1, 'Female': 0, 'Male': 1}, inplace = True)