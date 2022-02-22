import numpy as numpy
import time as time

print("STARTED...")

multiple = 750000000

data = numpy.random.rand(multiple)

tic = time.perf_counter()

sorted = numpy.sort(data, kind="stable")

toc = time.perf_counter()

"""
for n in sorted:
    num = int(round(n * multiple))
    print(num)
    """

print(f"in {toc - tic:0.4f} seconds")
print("FINISHED")
