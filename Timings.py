import numpy as np
import matplotlib.pyplot as plt


python_5000 = 50
python_500000 = 100
python_5000000 = 200
c_debug_5000 = 1
c_debug_500000 = 2
c_debug_5000000 = 3
c_release_5000 = 4
c_release_500000 = 5
c_release_5000000 = 6


height = [python_5000, python_500000, python_5000000, c_debug_5000, c_debug_500000, c_debug_5000000, c_release_5000, c_release_500000, c_release_5000000]
bars = ('Python 5.000', 'Python 500.000', 'Python 5.000.000', 'c++ debug 5.000', 'c++ debug 500.000', 'c++ debug 5.000.000', 'c++ release 5.000', 'c++ release 500.000', 'c++ release 5.000.000')
y_pos = np.arange(len(bars))
plt.bar(y_pos, height, color=['green', 'orange', 'red'])
plt.xticks(y_pos, bars, rotation=270)
plt.show()