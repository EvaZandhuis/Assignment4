import numpy as np
import matplotlib.pyplot as plt

# with printing:
# python_5000 = 0.2980223000049591
python_5000 = 0.1320603999774903
python_500000 = 6.281164800049737
python_5000000 = 56.26100910000969
python_50000000 = 671.736297299969
c_debug_5000 = 1
c_debug_500000 = 2
c_debug_5000000 = 3
c_debug_50000000 = 4
c_release_5000 = 5
c_release_500000 = 6
c_release_5000000 = 7
c_release_50000000 = 8


height = [python_5000, python_500000, python_5000000, python_50000000, c_debug_5000, c_debug_500000, c_debug_5000000, c_debug_50000000, c_release_5000, c_release_500000, c_release_5000000, c_release_5000000]
bars = ('Python 5.000', 'Python 500.000', 'Python 5.000.000', 'Python 50.000.000', 'c++ debug 5.000', 'c++ debug 500.000', 'c++ debug 5.000.000', 'c_debug_50.000.000', 'c++ release 5.000', 'c++ release 500.000', 'c++ release 5.000.000', 'c_release_50.000.000')
y_pos = np.arange(len(bars))
plt.bar(y_pos, height, color=['green', 'orange', 'red', 'black'])
plt.xticks(y_pos, bars, rotation=270)
plt.show()