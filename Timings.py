import numpy as np
import matplotlib.pyplot as plt
iterations = ['5000','500000','5000000','50000000']
programmes= ['Python', 'C++ Debug', 'C++ Release']
pos = np.arange(len(iterations))
bar_width = 0.25
python=[0.132,6.281,56.261,671.736]
cdebug=[0.629,0.735,7.302,73.079]
crelease=[0.055,0.115,0.727,5.952]
plt.bar(pos,python,bar_width,color='blue',edgecolor='black')
plt.bar(pos+bar_width,cdebug,bar_width,color='pink',edgecolor='black')
plt.bar(pos+2*bar_width,crelease,bar_width,color='red',edgecolor='black')
plt.xticks(pos, iterations)
plt.xlabel('Instance size', fontsize=16)
plt.ylabel('Run time [s]', fontsize=16)
plt.title('Comparison Python, C++ Debug and C++ Release',fontsize=16)
plt.legend(programmes,loc=2)
plt.show()
