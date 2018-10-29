import pandas as pd


#fields = ['date']
df_raw = pd.read_csv('sales_train_v2.csv', skipinitialspace=True)

def monthofyear(monthInt):
    monthWords = 'Undefined'
    if monthInt == 1:
        monthWords  = 'January'
    elif monthInt == 2:
        monthWords  = 'February'
    elif monthInt == 3:
        monthWords  = 'March'
    elif monthInt == 4:
        monthWords  = 'April'
    elif monthInt == 5:
        monthWords  = 'May'
    elif monthInt == 6:
        monthWords  = 'June'
    elif monthInt == 7:
        monthWords  = 'July'
    elif monthInt == 8:
        monthWords  = 'August'
    elif monthInt == 9:
        monthWords  = 'September'
    elif monthInt == 10:
        monthWords  = 'October'
    elif monthInt == 11:
        monthWords  = 'November'
    elif monthInt == 12:
        monthWords  = 'December'
    return monthWords


# -- ADD COLUMN add month of the year column
df_raw['monthint'] = df_raw['date'].str.split('.').str[1].astype(int)
df_raw['monthwords'] = df_raw['monthint'].apply(monthofyear)
#print(df_raw.head())
# -- Aggregate by shopId,item_id & month
df_aggregate = pd.DataFrame()
df_aggregate = df_raw.groupby(['shop_id','item_id','date_block_num','monthint'], as_index=False).agg({"item_cnt_day": "sum"})
df_aggregate = df_aggregate.rename(columns={'item_cnt_day': 'item_cnt_month'})
df_aggregate['monthwords'] = df_aggregate['monthint'].apply(monthofyear)
df_aggregate = df_aggregate.drop(['monthint'], axis=1)
print(df_aggregate.head())


# pd.set_option('max_rows',25)
# pd.set_option('max_columns',7)
df_aggregate_33 = pd.DataFrame()
df_aggregate_33 = df_aggregate[df_aggregate['date_block_num'] == 33]
#print(df_aggregate_33)

pd.set_option('max_columns',12)
df_aggregate_1_32 = pd.DataFrame()
df_aggregate_1_32 = df_aggregate[df_aggregate['date_block_num'] != 33]
#print(df_aggregate_1_32.tail())

df_dummies = df_raw['monthwords']
df_dummies = pd.get_dummies(df_dummies)
#print(df_dummies.tail())


#df_temp1 = pd.DataFrame()
# df_temp['monthwords'] = df_temp['monthint'].apply(monthofyear)

#print(df_raw.head())

#print(df_raw.tail())
