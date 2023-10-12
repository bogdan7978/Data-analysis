#### Plotting with Matplotlib | lines plots

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
  1. `c = 'b' ` - Set the color of the line, [supported colors](https://matplotlib.org/stable/gallery/color/named_colors.html)
  2. `ls = '--'` - Change between a solid or dashed line
  3. `lw = 2` - Set the width of a line
  4. `ms = 5` - Size of markers
  5. `mec = 'r'` - Set the edge color for markers
  6. `mew = 5` - Set the edge width for markers
  7. `mfc = 'g'` - Set the infill color for markers
  8. `alpha = 0.5` - Opacity of the plot

- The `fmt` argument allows to select the the marker type, line type and color. It is the 3rd argument for `plt.plot()`
`plt.plot(df1, df2, 's-r')`

- To change the size of the graph
`plt.figure(figsize(5, 6))`

#### Using seaborn to improve the design
`import seaborn as sns`

- Using predefined [styles](https://seaborn.pydata.org/generated/seaborn.set_style.html)
`sns.set_style('whitegrid')

- Changing the style using matplotlib 
`matplotlib.rcParams`

#### Scatter plots
> Values of 2 variables plotted as 2 points, without being joined by a line

`sns.scatterplot(df1, df2)`

- Adding a `hue` to the plot that will make it more intuitive
`sns.scatterplot(flowers_df.sepal_length, flowers_df.sepal_width, hue=flowers_df.species, s=100) # `s` is the size of the points

> When using `sns` plot, `plt` funcions can be added, and viceversa

#### Histogram
> A histogram is usually used to display one column. It counts how many values fall in a range of the column values using bars

`plt.hist(flowers_df.sepla_width);`

- Controlling the graph
```python
plt.hist(flowers_df.sepla_width, bins=5); # displays only 5 bins
plt.hist(flowers_df.sepla_width, bins=np.arrange(2, 5, 0.25); # bins form 2 to 4, incremented by 0.25
plt.hist(flowers_df.sepla_width, bins=[1, 3, 4, 4.5]; # bins form 1 to 3, 3 to 3, and 4 to 4.5
```

- 2 histograms can be plotted together in the same graph, using the `alpha=` to reduce the opacity
```python
plt.hist(flowers_df.2, alpha=0.4, bins=5); 
plt.hist(flowers_df.1, alpha=0.4, bins=5);
```

- Stacking histograms on top of each other
```python
plt.hist(flowers_df.1, flowers_df.2, flowers_df.3
         bins=5, stacked=True);
```
#### Bar charts

`plt.bar(years, oranges);`
> Line chart can be added on the bar chart `plt.plot()`




