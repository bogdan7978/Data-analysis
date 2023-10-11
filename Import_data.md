#### To read from a database
```python
pip install sqlalchemy
import sqlite3
```

- Query method
```python
conn = sqlite3.connect('chinook.db')
df = pd.read_sql_query('SELECT * FROM employees;', conn)

df = pd.read_sql_query('SELECT * FROM employees;', conn,
                 index_col='EmployeeId',
                 parse_dates=['BirthDate', 'HireDate'])
```

- Table method
```python
from sqlalchemy import create_engine
engine = create_engine('sqlite:///chinook.db')

connection = engine.connect()
df = pd.read_sql_table('employees', con=connection)
```

#### CSV

- Website
```python
csv_url = "https://raw.githubusercontent.com/datasets/gdp/master/data/gdp.csv"
pd.read_csv(csv_url).head()
```

- Local file
```python
df = pd.read_csv('btc-market-price.csv')
df.head()
```

- Multiple parameters passed
```python
df = pd.read_csv('btc-market-price.csv',
                 header=None,
                 na_values=['', '?', '-'],
                 names=['Timestamp', 'Price'],
                 dtype={'Price': 'float'},
                 parse_dates=[0],
                 index_col=[0])
```

`pd.read_csv?` to see more info about the parameters 
