import numpy as np

"""
Exercise 1: Create a 4X2 integer array and Prints its attributes: shape, dimension and length in bytes
"""
array = np.empty([4, 2], dtype=np.int16)
print("1. The shape of an array: ", array.shape)
print("2. Array dimensions: ", array.ndim)
print("3. The Length of each element of the array in bytes: ", array.itemsize)
print("----------------------------------")


"""
Exercise 2: Create a 5X2 integer array from a range between 100 to 200 such that the difference between each element is 10
"""
array = np.arange(100, 200, 10, dtype=int)
array = array.reshape(5, 2)
print(array)
print("----------------------------------")


"""
Exercise 3: Following is the provided numPy array. Return array of items by taking the third column from all rows
"""
sampleArray = np.array([[11, 22, 33], [44, 55, 66], [77, 88, 99]])
print(sampleArray[..., 2])
print("----------------------------------")


"""
Exercise 4: Return array of odd rows and even columns from below numpy array
"""
sampleArray = np.array(
    [
        [3, 6, 9, 12],
        [15, 18, 21, 24],
        [27, 30, 33, 36],
        [39, 42, 45, 48],
        [51, 54, 57, 60],
    ]
)
print(sampleArray[::2, 1::2])
print("----------------------------------")


"""
Exercise 5: Create a result array by adding the following two NumPy arrays. Next, modify the result array by calculating the square of each element
"""
arrayOne = np.array([[5, 6, 9], [21, 18, 27]])
arrayTwo = np.array([[15, 33, 24], [4, 7, 1]])

res_np = arrayOne + arrayTwo
result_squared = np.vectorize(lambda x: x * x)(res_np)
print(result_squared)
print("----------------------------------")


"""
Exercise 6: Split the array into four equal-sized sub-arrays

Note: Create an 8X3 integer array from a range between 10 to 34 such that the difference between each element is 1 and then Split the array into four equal-sized sub-arrays.
"""
array = np.arange(10, 34, 1, dtype=int).reshape(8, 3)
print(np.array_split(array, 4))
print("----------------------------------")


"""
Exercise 7: Sort following NumPy array

    Case 1: Sort array by the second row
    Case 2: Sort the array by the second column
"""
sampleArray = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])
sort_by_row = sampleArray[:, sampleArray[1, :].argsort()]
sort_by_col = sampleArray[sampleArray[:, 1].argsort()]
print(sort_by_row)
print(sort_by_col)
print("----------------------------------")


"""
Exercise 8: Print max from axis 0 and min from axis 1 from the following 2-D array.
"""
sampleArray = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])
print(np.amin(sampleArray, 1))
print(np.amax(sampleArray, 0))
