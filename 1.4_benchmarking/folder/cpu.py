import time 
import MacTmp
import psutil

def cpu_stress(n = 10_000):
    total = 0
    for i in range(n):
        total = i * i
        print(total)
    print(MacTmp.CPU_Temp())
    print(psutil.cpu_percent(interval=1), '%')
start = time.perf_counter()
cpu_stress()
end = time.perf_counter()
print('Execution time:', end - start, 'seconds')
