"""
- Write a function that takes in some array of at least 3 integers and returns an array of the three largest integers in this input array
- Caveat - implement this function without sorting the input array - you cannot sort, only traverse
- Hint - can you keep track of the three largest numbers in our array as you traverse the input array
- Important - the function can return duplicate integers if there are any
- For example, if your input array is: [11, 4, 8, 11, 15], result will be [11, 11, 15]
"""


array1 = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7] # result = [18, 141, 541]
array2 = [8, 8, 8, 8, 8, 8, 8, 8, 10, 8, 8, 8, 8, 8] # result  = [8, 8, 10]
array3 = [1, 1, 1, 1, 1, 1, 1, 1] # result = [1, 1, 1]
array4 = [-1, -2, -3, -7, -17, -27, -18, -541, -8, -7, 7] # result = [-2, -1, 7]


# simple solution - doesn't account for all being negative, not very efficient
def find_3_largest_nums(array):
    largest_three = [] # store the largest numbers
    for i in range(0, 3): # repeat the process three times to find the first, second and third largest
        max1 = 0
        for j in range(len(array)): # find largest in current array
            if array[j] > max1:
                max1 = array[j] # loop through and update max1 each time if larger value found
        array.remove(max1) # remove largest number found
        largest_three.append(max1) # store the largest number
    return largest_three[::-1] # reverse the new list


print(find_3_largest_nums(array1))
print(find_3_largest_nums(array2))
print(find_3_largest_nums(array3))
# print(largest_three_numbers(array4)) won't work for the above

"""
Better version
"""

def find_3_largest_nums(array):
 largest_3 = [float("-inf"), float("-inf"), float("-inf")]
 for num in array:

  if num >= largest_3[2]:
   largest_3[0] = largest_3[1]
   largest_3[1] = largest_3[2]
   largest_3[2] = num

  elif num >= largest_3[1]:
   largest_3[0] = largest_3[1]
   largest_3[1] = num

  elif num >= largest_3[0]:
   largest_3[0] = num
 return largest_3

array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]

print(find_3_largest_nums(array))

#####################################################

# Case 2, result = [8, 8, 10]
array = [8, 8, 8, 8, 8, 8, 8, 8, 10, 8, 8, 8, 8, 8]
print(find_3_largest_nums(array))

#####################################################

# Case 3, result = [1, 1, 1]
array = [1, 1, 1, 1, 1, 1, 1, 1]
print(find_3_largest_nums(array))

####################################################

# Case 4, result = [-2, -1, 7]
array = [-1, -2, -3, -7, -17, -27, -18, -541, -8, -7, 7]
print(find_3_largest_nums(array))

####################################################