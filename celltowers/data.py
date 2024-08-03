import pandas as pd
df=pd.read_csv('5g_coverage.csv')
output_csv='Vodafone.csv'
filter_df=df[(df['operator']=='Vodafone Idea')]
india_df = filter_df[
    (filter_df['latitude'] >= 6.8) & (filter_df['latitude'] <= 37.6) &          # longitude and latitude extent of India
    (filter_df['longitude'] >= 68.7) & (filter_df['longitude'] <= 97.25)
]
india_df.to_csv(output_csv,index=False)
print(india_df.info())