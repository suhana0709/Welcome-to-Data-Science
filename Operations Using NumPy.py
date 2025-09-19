#import libraries
import numpy as np

print("*******Operetions Using NumPy**********\n")

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print("Original array:-\n",arr)
newarr = arr.reshape(4, 3)
print("New Array:-\n",newarr)

a = np.array([10, 10, 10])
print("\nAnother Array:-    ",a)

#addition
print("\nAddition between the 'new array' and the 'another array:-")
add = np.add(newarr, a)
print("\n", add)