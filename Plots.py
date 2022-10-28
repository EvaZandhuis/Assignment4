import numpy as np
import matplotlib.pyplot as plt

# X-axis values
x = [5000,500000,5000000,50000000]

# Y-axis values
y1 = [0.132,6.281,56.261,671.736]
# Y-axis values
y2 = [0.629,0.735,7.302,73.079]
# Y-axis values
y3 = [0.055,0.115,0.727,5.952]
# Function to plot
#plt.axis([0, 50000000, 0, 800])
plt.scatter(x, y1, label ="Python")
plt.scatter(x, y2, label ="C++ Debug")
plt.scatter(x, y3, label ="C++ Release")

# Function add a legend
plt.legend(bbox_to_anchor =(0.75, 1.15), ncol = 2)

# function to show the plot
plt.show()