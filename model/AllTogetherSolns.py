import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error


df = pd.read_csv('../raw_data/survey_results_public.csv')
schema = pd.read_csv('../raw_data/survey_results_schema.csv')


