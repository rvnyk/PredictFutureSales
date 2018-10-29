# import pandas as pd

from fastai.imports import *
from fastai.structured import *
df_raw = pd.read_csv('sales_train_v2.csv', skipinitialspace=True)

def display_all(df):
    with pd.option_context("display.max_rows", 1000, "display.max_columns", 1000):
        print(df)

display_all(df_raw.tail().T)


add_datepart(df_raw, 'date')

display_all(df_raw.tail().T)