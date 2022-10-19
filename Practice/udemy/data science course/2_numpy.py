import numpy as np

my_list = [1, 2, 3]

arr = np.array(my_list)

my_mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

arr2 = np.array(my_mat)

# print(arr2)

lst = np.arange(0, 11)
# print(lst)

np.zeros((2, 3))

print(np.linspace(0, 5, 10))

print(np.random.rand(5, 5))

print(np.random.randn(4, 4))

print(np.random.randint(1, 100, 10))

arr = np.arange(25)
ranarr = np.random.randint(0, 50, 10)
print(arr.reshape(5, 5))
