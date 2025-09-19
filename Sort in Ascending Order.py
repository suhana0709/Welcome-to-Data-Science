#import libraries
import numpy as np

data_type = [('name', 'S15'), ('class', int), ('height', float)]
student_details = [('James', 5, 42.5), ('Sirius', 5, 40.5), ('Lupin', 6, 43.5)]

#creating a structured array
students = np.array(student_details, dtype=data_type)
print("Original Array:-\n",students)

print("Sort by height:-")
print(np.sort(students, order='name'))