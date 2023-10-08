## Series
```python
### CREATE, NAME, VALUES, INDEX
s = pd.Series(['A', 'B', 'C']) 
s.name = 'letters' 
s.values 
s.index = ['first', 'second', 'third']

## First item
X[0] # by position
X.iloc[0] # by position
X['first'] # by index

## Last item
X[-1] # by position
X.iloc[-1] # by position
X['third'] # by index

X.iloc[1:-1] # middle elements

## Reverse order 
X.iloc[::-1]
X[::-1]

## First and last
X[['first', 'fifth']]
X.iloc[[0, -1]]
X[[0, -1]]

## CONVERT TO FLOAT
pd.Series(X, dtype=float) 

## SORT ORDER
X = X.sort_values()  
```

## Boolean or masks

```
##### SHOW NEGATIVE ELEMENTS
`X = pd.Series([-1,2,0,-4,5,6,0,0,-9,10])
`mask = X < 0 

##### GET NEGATIVE VALUES
`X[mask]` 

##### NR HIGHER THAN MEAN
`mask = X > X.mean()
`X[mask]` 

##### NR EQUAL TO 2 OR 10
`mask = (X == 2) | (X == 10)
`X[mask]` 
```


#### Logic functions
```
X.all() # returns true if no element is 0
X.any() # returns true if there is an 0

```

#### Summary statistics
```
X.sum() # sum of elements
X.mean() # average of elements
X.max()
X.min()
```

![purple-divider](https://user-images.githubusercontent.com/7065401/52071927-c1cd7100-2562-11e9-908a-dde91ba14e59.png)

## Data frames

```
df.iloc = [[1, -1]]  # show the positions (second element and last)
df.iloc = [1:-1] # show form the second until the last
```

```
df = pd.DataFrame()

df.shape # how many columns and rows
df.info()
df.describe()
df.dtypes
df.size

df.head(3) # show first 3 rows
df.tail(3) # show the last 3 rows

# add column names
df.columns = ['first', 'second']

# drop the column 'name' | replace axis=0 for row
df = df.drop(['name'], axis=1)

# assign index
df.index = df['name'] 

# show first 5 elements form Sex column
marvel_df.iloc[:5,].Sex.to_frame()
marvel_df.head().Sex.to_frame()

# show middle elements form Born column
marvel_df.iloc[1: -1].Born.to_frame()

df.loc = ['row', 'column'] = 129 # change the value of a row and column

## ADD a new column that is the result of a calculus with another column
marvel_df['years_since'] = 2023 - marvel_df['Born']

## SHOW the male characters
mask = marvel_df['Sex'] == 'male'
marvel_df[mask] | mask  # first one shows only male chr, second shows all

## characters born after 1970 and female
mask = (marvel_df['Sex'] == 'female') & (marvel_df['Born'] > 1970)
marvel_df[mask]

## RESET INDEX
df = df.reset_index()

## SET INDEX
df.set_index('Population')

## ADD VALUES
df.loc['China'] = pd.Series({'Population': 1_400_000_000, 'Continent': 'Asia'})

## DELETE COLUMN
df.drop(columns='Language', inplace=True)

## DELETE ROW
df.drop('China', inplace=True)

## Modify 
marvel_df.loc['Vision', 'Born'] = 1964
```

> If your DatetimeIndex is not sorted, you can sort it using the `sort_index()` method
`df.sort_index(inplace=True)`
#### Plotting
```
# Plot the values of a column
df.ColumnName.plot()


```
