import pandas as pd

df = pd.read_csv("raw/data.csv")

def show_columns(df):
	return df.columns

def check_nan(df, col):
	return df[col].isna().any().any()