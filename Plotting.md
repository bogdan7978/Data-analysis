#### Plotting with Matplotlib

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline # creates a new line for plots
```

- Simple plot
`plt.plot(df);`

- Plotting 2 determined axis with labels
```python
plt.plot(df1, df2)
plt.xlabel('description')
plt.yplabel('description');
```
- Plotting 2 lines on the same graph
```python
plt.plot(df1, df2)
plt.plot(df1, df3)
plt.xlabel('description')
plt.yplabel('description')
```
- ADD title and legend to the graph
```python
plt.title("title of chart")
plt.legend(['df2', 'df3']);
```
- ADD markers to the plot
`plt.plot(df1, df2, marker=".")`
> Full marker list can be found [here](https://matplotlib.org/stable/api/markers_api.html)

- Customization of lines and markers for `plt.plot()`
  1. `c = 'b' ` - Set the color of the line
  2. `ls = '--'` - Change between a solid or dashed line
  3. `lw = 2` - Set the width of a line
  4. `ms = 5` - Size of markers
  5. `mec = 'r'` - Set the edge color for markers
  6. `mew = 5` - Set the edge width for markers
  7. `mfc = 'g'` - Set the infill color for markers
  8. `alpha = 0.5` - Opacity of the plot
