"""
Have the function OffLineMinimum(strArr) take the strArr parameter being passed which will be an array of integers ranging from 1...n and the letter "E" and return the correct subset based on the following rules.
The input will be in the following format: ["I","I","E","I",...,"E",...,"I"] where the I's stand for integers and the E means take out the smallest integer currently in the whole set.
When finished, your program should return that new set with integers separated by commas.
For example: if strArr is ["5","4","6","E","1","7","E","E","3","2"] then your program should return 4,1,5.

Examples:
Input: ["1","2","E","E","3"]
Output: 1,2

Input: ["4","E","1","E","2","E","3","E"]
Output: 4,1,2,3
"""

def OffLineMinimum(strArr):
  sorted_nums = [] # store nums in sorted order
  result = [] # store numbers output by E

  for item in strArr:
    if item == "E":
      if sorted_nums: # check if any nums in sorted_nums
        result.append(str(sorted_nums.pop(0))) # remove and add to smallest
    else:
      num = int(item)
      # insert new num into sorted position
      inserted = False
      for i in range(len(sorted_nums)):
        if num < sorted_nums[i]:
          sorted_nums.insert(i, num)
          inserted = True
          break
      if not inserted:
        sorted_nums.append(num)
  return ",".join(result)

# keep this function call here
# print(OffLineMinimum(input()))

# Testing:
arr1 = ["1","2","E","E","3"] # "1,2"
arr2 = ["4","E","1","E","2","E","3","E"] # "4,1,2,3"
arr3 = ["5","4","6","E","1","7","E","E","3","2"] # "4,1,5"

print(OffLineMinimum(arr1))
print(OffLineMinimum(arr2))
print(OffLineMinimum(arr3))