import numpy as np

prices_list = [148.50, 150.25, 149.80, 152.10, 151.75]
prices_array = np.array(prices_list)

print(prices_list)
print(prices_array)
print(type(prices_list))
print(type(prices_array))

print(prices_array.shape)   # how many elements, in what dimensions
print(prices_array[0])       # first element — same as a list
print(prices_array[-1])      # last element — same as a list
print(prices_array[1:3])     # slicing — also same as a list


prices_list = [148.50, 150.25, 149.80, 152.10, 151.75]
doubled = prices_list * 2
print(doubled)

prices_array = np.array(prices_list)
doubled = prices_array * 2
print(doubled)

prices_array = np.array([148.50, 150.25, 149.80, 152.10, 151.75])

returns = prices_array[1:] / prices_array[:-1] - 1
print(returns)

print(f"Mean return: {returns.mean():.4f}")
print(f"Std dev (volatility): {returns.std():.4f}")
print(f"Min return: {returns.min():.4f}")
print(f"Max return: {returns.max():.4f}")

# A vector — just a 1D array
v = np.array([1, 2, 3])
print(v)
print(v.shape)

# A matrix — a 2D array
M = np.array([[1, 2], [3, 4]])
print(M)
print(M.shape)

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(A @ B)
print(A * B)   # element-by-element multiplication
print(A @ B)   # true matrix multiplication

C = np.array([[1, 2, 3], [4, 5, 6]])
print(C)
print(C.shape)

print(C.T)
print(C.T.shape)
