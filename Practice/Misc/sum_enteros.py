import time as time

tic = time.perf_counter()

n = input("\ndame un num: ")

num = list(range(1, int(n) + 1))

ans = 0
for i in num:
  ans += num[i-1]

toc = time.perf_counter()
print(f"\n{ans}")
print(f"\nin {toc - tic:0.2f} seconds")
print("\nDONE")