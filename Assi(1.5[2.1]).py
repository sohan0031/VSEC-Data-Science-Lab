import numpy as np

first_array = np.array([3, 9, 27, 81])
second_array = np.array([2, 4, 8, 16])

result1 = first_array + second_array
result2 = first_array - second_array
result3 = first_array * second_array
result4 = first_array / second_array

print("Using the + operator:",result1) 
print("Using the - operator:",result2) 
print("Using the * operator:",result3) 
print("Using the / operator:",result4) 


result5 = np.add(first_array, second_array)
result6 = np.subtract(first_array, second_array)
result7 = np.multiply(first_array, second_array)
result8 = np.divide(first_array, second_array)

print("Using the add() function:",result5) 
print("Using the subtract() function:",result6) 
print("Using the multiply() function:",result7) 
print("Using the divide() function:",result8) 
