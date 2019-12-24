- isna(), notna()
- x.groupby('sex').size()
```py
for col in data.columns:
    series = data[col]

pd.data_range('20130101', periods=6)

pd.DataFrame(np.random.randn(3,5), index=pd.date_range('20130101', periods=3), columns=list('abcde'))

pd.DataFrame().dtypes
pd.DataFrame().index
pd.DataFrame().columns
pd.DataFrame().to_numpy()
pd.DataFrame().sort_index(axis=1, ascending=False)
pd.DataFrame().sort_values(by='B')

data.loc[0:10, ['专利名称', '专利权人']]
data.loc[0, '专利名称'] == data.at[0, '专利名称']
data.iloc[1, 1]
data.iloc[1:2, 3:5]
data.iloc[[1,2], [3,4]]

df2[df2['E'].isin(['two', 'four'])]

data.reindex(index=x, columns=list('ancd') + ['e'])
data.dropna(how='any')
data.fillna(value=5)
pd.isna(data)

pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)

pd.Series.value_counts()

df = pd.DataFrame(np.random.randn(10, 4))  
pieces = [df[:3], df[3:7], df[7:]]
pd.concat(pieces)
```

