import time, numpy as np
start = time.perf_counter()
a = np.random.randint(0, 10_000_000)
end = time.perf_counter()
print(a)
print('Memory allocation time:', end - start)
