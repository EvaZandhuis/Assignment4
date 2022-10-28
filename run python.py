# import matplotlib.pyplot as plt
from time import perf_counter
import subprocess
duration = []

n_list = [5000]
path = r"C:\Users\there\Assignment4\nbody.py"
for i in n_list:
    start_time = perf_counter()
    subprocess.check_call(['python.exe', path, str(i)])
    stop_time = perf_counter()
    duration.append((stop_time - start_time))
print('duration =', duration)
print("Elapsed time during the whole program in seconds:",
      stop_time - start_time)
