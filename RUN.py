import matplotlib.pyplot as plt
from time import perf_counter
import subprocess
duration = []
argument = 0
n_list = [5000, 50000, 500000, 5000000]
path = r"C:\Users\there\Assignment4\cmake-build-release\nbody.exe"
for i in n_list:
    start_time = perf_counter()
    subprocess.check_call([path, str(i), str(argument)])
    stop_time = perf_counter()
    duration.append((stop_time - start_time))
print(duration)
print("Elapsed time during the whole program in seconds:",
      stop_time - start_time)
