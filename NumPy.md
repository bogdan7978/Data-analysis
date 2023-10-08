> **A library for python that works in the back and not used very often, it help a lot with computation and saves a ton of memory**

### Arrays

```python
A.size
A.dtype
A.shape
A.ndim
A.sum
A.mean
A.std
A.var
A.sum(axis=0)
A.mean(axis=1)
```

```python
A = np.array ([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

  row   column
A[: , 1:2] # every row, second number
A[1, 2]  # second row, third column
A[:2, :2] # :x everything before
A[1:, 1:] # x: everything after
```

```python
A[1] = np.array([10, 10, 10]) # replace the second row with these values
A[2] = 99 # same operation for row 2
```


- Matrix 3*3 with ones on the diagonal and zeros elswhere
`np.identity(3) or np.eye(3)`

- Numpy array filled with 3 random integers form 1 to 10
`np.random.randint(10, size=3)`

- Random float matrix 3*3*3
`np.random.randn(3,3,3)`

- Array that skips form 2 to 2 nr
`np.arange(0, 11, 2)`

- Array except the last 2 numbers
`np.arange(1, 11)[: -2]`

- Array in decending order
`np.arange(1, 11)[::-1]`

- 3*3 matrix filled with values from 0 to 8
`np.arange(9).reshape(3,3)`

- Show the elements in reverse order
```python
X = np.array(['A','B','C','D','E'])
X[::-1]
```

- Show elements in an even position
```python
X = np.array(['A','B','C','D','E'])
X[1::2]
```

- Show elements in an odd position
```python
X = np.array(['A','B','C','D','E'])
X[::2]
```

- Reverse a give array
```python
X = [-5, -3, 0, 10, 40]
X[::-1]
```

- Sort the given array
`X.sort()`

- Set fifth element to number 5
`X[4] = 5`

### Broadcasting and vectorized operations
```python
a = np.arrange(4) --> a([0,1,2,3])
a + 10 --> a([10,11,12,13]) # creates a new array
a += 1 # modifies the initial array
a + b # adding 2 similar arrays

a[[True, False, False, True]] # selecting first and last element using Boolean

a >= 2 # results Booleans
a[a >= 2] # create a new array
```

### Mask

- Given the X numpy array, get numbers higher than 5
```python
X = np.array([-1, 2, 0, -4, 5, 6, 0, 0, -9, 10])

mask = X > 5
X[mask]
```

- Given the X numpy array, make a mask showing negative elements
```python
X = np.array([-1,2,0,-4,5,6,0,0,-9,10])

mask = X <= 0
mask
```

- Given the X numpy array, get the negative elements
```python
X = np.array([-1, 2, 0, -4, 5, 6, 0, 0, -9, 10])

mask = X <= 0
X[mask]
```

### Boolean operators
```
~ # is not
| # OR
& # AND
```

### Size of obj in memory

**Python**

`sys.getsizeof(1) # check the size of an int in memory`

**NumPy**
```python
np.dtype(int).itemsize # int size

print("%d bytes" % (Z.size * Z.itemsize)) # array size
```
