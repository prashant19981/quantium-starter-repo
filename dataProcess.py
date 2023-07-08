import pandas as pd


sales_df_0 = pd.read_csv("data/daily_sales_data_0.csv")
sales_df_1 = pd.read_csv("data/daily_sales_data_1.csv")
sales_df_2 = pd.read_csv("data/daily_sales_data_2.csv")
tempdf = sales_df_1.groupby(['date'])
full_sales_df = pd.concat([sales_df_0,sales_df_1,sales_df_2])
pink_morsels_data = full_sales_df[full_sales_df['product'] == 'pink morsel']
pink_morsels_data['price'] = pink_morsels_data['price'].str.replace('$','').astype(float)
pink_morsels_data['Sales'] = pink_morsels_data['price']*pink_morsels_data['quantity']
print(pink_morsels_data)
pink_morsels_data = pink_morsels_data.drop(['product','price','quantity'], axis=1)
pink_morsels_data.to_csv('output.csv',index=False)

