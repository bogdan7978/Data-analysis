#### To read from an database
`pip install sqlalchemy`
`import sqlite3`
query method
```
conn = sqlite3.connect('chinook.db')
df = pd.read_sql_query('SELECT * FROM employees;', conn)

df = pd.read_sql_query('SELECT * FROM employees;', conn,
                 index_col='EmployeeId',
                 parse_dates=['BirthDate', 'HireDate'])


```

table method
```
from sqlalchemy import create_engine
engine = create_engine('sqlite:///chinook.db')

connection = engine.connect()
df = pd.read_sql_table('employees', con=connection)
```


#### CSV

website
```
csv_url = "https://raw.githubusercontent.com/datasets/gdp/master/data/gdp.csv"

pd.read_csv(csv_url).head()
```

local file
```
df = pd.read_csv('btc-market-price.csv')

df.head()
```

multiple parameters passed
```
df = pd.read_csv('btc-market-price.csv',
                 header=None,
                 na_values=['', '?', '-'],
                 names=['Timestamp', 'Price'],
                 dtype={'Price': 'float'},
                 parse_dates=[0],
                 index_col=[0])
```

`pd.read_csv?` to see more info about the parameters 
