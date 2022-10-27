import matplotlib.pyplot as plt
from time import perf_counter
import subprocess
duration = []

n_list = [5000, 500000, 5000000, 50000000]
path = r"C:\Users\Eva\Documents\TU\Master\Python programming\nbody\nbody.py"
for i in n_list:
    start_time = perf_counter()
    subprocess.check_call(['python.exe', path, str(i)])
    stop_time = perf_counter()
    duration.append((stop_time - start_time))
print('duration =', duration)
print("Elapsed time during the whole program in seconds:",
      stop_time - start_time)
plt.plot(n_list, duration)
plt.xlabel("x")
plt.ylabel("y")
#plt.loglog()
plt.show()