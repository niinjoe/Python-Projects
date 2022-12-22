import numpy as np

my_list = [1, 2, 3]

arr = np.array(my_list)

my_mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

arr2 = np.array(my_mat)

# print(arr2)

lst = np.arange(10, 51)
# print(lst)

np.zeros((2, 3))

# print(np.linspace(0, 5, 10))

# print(np.random.rand(5, 5))

# print(np.random.randn(4, 4))

# print(np.random.randint(1, 100, 10))

arr = np.arange(25)
ranarr = np.random.randint(0, 50, 10)
# print(ranarr.reshape(5, 5))

ran = np.random.random(25)
# print(ran)


# print(ranarr.max)
# print(ranarr.min())
# print(ranarr.argmax())
# print(ranarr.argmin())

arr_2d = np.array([[5, 10, 5], [20, 25, 30], [35, 40, 45]])
arr2d = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
arr2d = np.array([])
# print(arr_2d[2,1])
# print(arr_2d[:2])

# arr = np.arange(1,11)
# print(arr)
# bool_arr = arr>5

# print(bool_arr)
# print(arr[bool_arr])

arr[arr > 5]

new_arr = np.arange(50).reshape(5, 10)
ara = np.arange(0, 1.1, 0.05).reshape(5, 4)
print(ara)

# print(new_arr[1:3,3:5])

arr = np.zeros((1, 10))
# print(arr)

arr = np.ones((1, 10)) * 5


# print(arr)
