import pandas as pd
import numpy as np

fields = ['shop_id','item_id','item_price','date']
df_raw = pd.read_csv('sales_train_v2.csv', skipinitialspace=True, usecols=fields)

shops = df_raw.shop_id.unique()
print("shops : " + str(np.sort(shops)))

print("number of shops : " + str(df_raw.shop_id.nunique()))

items = df_raw.item_id.unique()
print("items : " + str(np.sort(items)))

print("number of items : " + str(df_raw.item_id.nunique()))

price = df_raw.item_price
dec = np.sort(price)
np.set_printoptions(formatter={'float': '{: 0.3f}'.format})
print(dec)




