## Series

- CREATE, NAME, VALUES, INDEX

```python
s = pd.Series(['A', 'B', 'C']) 
s.name = 'letters' 
s.values 
s.index = ['first', 'second', 'third']
```
- First item
```python
X[0] # by position
X.iloc[0] # by position
X['first'] # by index
```

- Last item
```python
X[-1] # by position
X.iloc[-1] # by position
X['third'] # by index
```
- Middle elements
`X.iloc[1:-1]`

- Reverse order 
```python
X.iloc[::-1]
X[::-1]
```

- First and last
```python
X[['first', 'fifth']]
X.iloc[[0, -1]]
X[[0, -1]]
```

- CONVERT TO FLOAT
`pd.Series(X, dtype=float)` 

- CONVERT obj type to numeric
```python
series2 = pd.to_numeric(series, errors='coerce')
```

- CONVERT series of lists to one series
```python
s = s.apply(pd.Series).stack().reset_index(drop=True)
```

- SORT ORDER
`X = X.sort_values()`  

- ADD new values to a series
```python
new_s = pd.concat([s, pd.Series([500, "php"])], ignore_index=True)
```
- CREATE subset of series
```python
n = 6
new_s = s[s < n]
```

- CHANGE order of index
```python
s = s.reindex(index = ['B','A','C','D','E'])
```

### Boolean or masks

- SHOW NEGATIVE ELEMENTS
```python
X = pd.Series([-1,2,0,-4,5,6,0,0,-9,10])
mask = X < 0
```

- GET NEGATIVE VALUES
`X[mask]` 

- NR HIGHER THAN MEAN
```python
mask = X > X.mean()
X[mask] 
```

- NR EQUAL TO 2 OR 10
```python
mask = (X == 2) | (X == 10)
X[mask] 
```

### Logic functions
```python
X.all() # returns true if no element is 0
X.any() # returns true if there is an 0
```

### Summary statistics
```
X.sum() # sum of elements
X.mean() # average of elements
X.max()
X.min()
```

![purple-divider](https://user-images.githubusercontent.com/7065401/52071927-c1cd7100-2562-11e9-908a-dde91ba14e59.png)

## Data frames

```python
df.iloc = [[1, -1]]  # show the positions (second element and last)
df.iloc = [1:-1] # show from the second until the last
```

```python
df = pd.DataFrame()

df.shape # how many columns and rows
df.info()
df.describe()
df.dtypes
df.size

df.head(3) # show first 3 rows
df.tail(3) # show the last 3 rows
```
- Add column names
`df.columns = ['first', 'second']`

- Drop the column 'name' | replace axis=0 for row
`df = df.drop(['name'], axis=1)`

- Assign index
`df.index = df['name']` 

- Show first 5 elements form Sex column
``` python
marvel_df.iloc[:5,].Sex.to_frame()
marvel_df.head().Sex.to_frame()
```

- Show middle elements form Born column
`marvel_df.iloc[1: -1].Born.to_frame()`

- Change the value of a row and column
`df.loc = ['row', 'column'] = 129`

- ADD a new column that is the result of a calculus with another column
`marvel_df['years_since'] = 2023 - marvel_df['Born']`

- SHOW the male characters
```python
mask = marvel_df['Sex'] == 'male'
marvel_df[mask] | mask  # first one shows only male chr, second shows all
```

- Characters born after 1970 and female
```python
mask = (marvel_df['Sex'] == 'female') & (marvel_df['Born'] > 1970)
marvel_df[mask]
```

- RESET INDEX
`df = df.reset_index()`

- SET INDEX
`df.set_index('Population')`

- ADD VALUES
`df.loc['China'] = pd.Series({'Population': 1_400_000_000, 'Continent': 'Asia'})`

- DELETE COLUMN
`df.drop(columns='Language', inplace=True)`

- DELETE ROW
`df.drop('China', inplace=True)`

- Modify 
`marvel_df.loc['Vision', 'Born'] = 1964`

> If your _DatetimeIndex_ is not sorted, you can sort it using the `sort_index()` method
`df.sort_index(inplace=True)`

- Group by
`tips_df.groupby('day')[['total_bill']].mean()`

- Change the columns and rows around
`.pivot(row, column, column)`
