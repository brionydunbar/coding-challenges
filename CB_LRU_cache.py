"""
Have the function LRUCache(strArr) take the array of characters stored in strArr, which will contain characters ranging from A to Z in some arbitrary order, and determine what elements still remain in a virtual cache that can hold up to 5 elements with an LRU cache algorithm implemented.
For example: if strArr is ["A", "B", "C", "D", "A", "E", "D", "Z"], then the following steps are taken:

(1) A does not exist in the cache, so access it and store it in the cache.
(2) B does not exist in the cache, so access it and store it in the cache as well.
So far the cache contains: ["A", "B"].
(3) Same goes for C, so the cache is now: ["A", "B", "C"].
(4) Same goes for D, so the cache is now: ["A", "B", "C", "D"].
(5) Now A is accessed again, but it exists in the cache already so it is brought to the front: ["B", "C", "D", "A"].
(6) E does not exist in the cache, so access it and store it in the cache: ["B", "C", "D", "A", "E"].
(7) D is accessed again so it is brought to the front: ["B", "C", "A", "E", "D"].
(8) Z does not exist in the cache so add it to the front and remove the least recently used element: ["C", "A", "E", "D", "Z"].

Now the caching steps have been completed and your program should return the order of the cache with the elements joined into a string, separated by a hyphen.
Therefore, for the example above your program should return C-A-E-D-Z.

Examples:
Input: ["A", "B", "A", "C", "A", "B"]
Output: C-A-B

Input: ["A", "B", "C", "D", "E", "D", "Q", "Z", "C"]
Output: E-D-Q-Z-C
"""

def LRUCache(strArr):
  cache = []
  for item in strArr:
    if item in cache:
      cache.remove(item) # if already there remove
      cache.append(item) # add to "front"
    else:
      if len(cache) > 4:
        del cache[0] # remove item at index 0
      cache.append(item) # add new item
    result = "" # initialise string for result
  for item in cache:
    result = result + item + "-"
  result = result[:-1] # remove final dash
  return result

# keep this function call here
# print(LRUCache(input()))

# Testing:
arr1 = ["A", "B", "A", "C", "A", "B"] # "C-A-B"
arr2 = ["A", "B", "C", "D", "E", "D", "Q", "Z", "C"] # "E-D-Q-Z-C"
arr3 = ["A", "B", "C", "D", "A", "E", "D", "Z"] # "C-A-E-D-Z"

print(LRUCache(arr1))
print(LRUCache(arr2))
print(LRUCache(arr3))