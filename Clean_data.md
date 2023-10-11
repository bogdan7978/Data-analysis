- Checking if a value is null or not
```python
pd.isnull(pd.Series([7, np.nan, 2]))
pd.notnull(pd.Series([7, np.nan, 2]))

Can be used as method as well - series.notnull()
# Both return True of False. Works with DataFrames as well
```
- The sum of null or not null values, returns an integer
```python
pd.isnull(series).sum()
pd.notnull(series).sum()
```

- Drop null values for series
`series.dropna()` # creates a new series, does not modify the initial one
- `.dropna()` used on DataFrames drops every row that contains minimum a null value, only keeps rows with no null values
  change to axis=1 to drop columns
- Threshold can be used, 'I need x valid values to keep the row/column'
`df.dropna(thresh=3)`

- Using the `.shape()` and `.info()` functions can get you a good picture of null values 

- Fill the null values
```python
s.fillna(0) #fill the null values with 0
s.fillna(s.mean()) #fill the null values with the mean
```
- Front fill and backwards fill
```python
s.fillna(method='ffill')  #fills the null values with the last known value form top
s.fillna(method='bfill') #fills the null values with the last known value form bottom
```

#### Finding unique values

`df.['Sex'].unique()` shows how many different values are
`df.['Sex'].value_counts()` shows how many values are and counts them

- Replacing
`df.['Sex'].replace('D', 'F')` replaces the D with F
`df.['Sex'].replace({'D' : 'F' , 'N' : 'M'})` replace the D with F and N with M

#### Duplications

`ambassadors.duplicated()` Returns boolean and goes from top to bottom
`ambassadors.duplicated(keep='last')`  Goes from bottom to top
`ambassadors.duplicated(keep=False)` Everything is considered duplicate

`ambassadors.drop_duplicates()` Drops the duplicates, can be used with the 'keep' method

`players.duplicated(subset=['Name'])` Only check in the column name

#### Splitting columns

`df.['Data'].str.split('_')` Splits the values that are separated by an underscore
`df.['Data'].str.split('_')` Creates a DataFrame form a series


