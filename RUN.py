import time
import subprocess
duration = []
print_to_file = 0
n_list = [5000, 50000]
path = r"C:\Users\there\Assignment4\cmake-build-release\nbody.exe"
for i in n_list:
    start_time = time.time()
    subprocess.check_call([path, str(i), str(print_to_file)])
    duration.append((time.time() - start_time))
print(duration)
