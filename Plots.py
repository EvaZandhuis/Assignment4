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
plt.scatter(x, y1, label ="Python", color='blue')
plt.scatter(x, y2, label ="C++ Debug",color='pink' )
plt.scatter(x, y3, label ="C++ Release",color='red')

# Function add a legend
plt.legend(bbox_to_anchor =(0.62, 1), ncol = 2)
plt.xlabel('Instance size', fontsize=16)
plt.ylabel('Run time [s]', fontsize=16)
plt.title('Comparison Python, C++ Debug and C++ Release',fontsize=16)

# function to show the plot
plt.show()