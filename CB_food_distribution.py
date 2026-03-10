"""
Have the function FoodDistribution(arr) read the array of numbers stored in arr which will represent the hunger level of different people ranging from 0 to 5 (0 meaning not hungry at all, 5 meaning very hungry).
You will also have N sandwiches to give out which will range from 1 to 20.
The format of the array will be [N, h1, h2, h3, ...] where N represents the number of sandwiches you have and the rest of the array will represent the hunger levels of different people.
Your goal is to minimize the hunger difference between each pair of people in the array using the sandwiches you have available.

For example: if arr is [5, 3, 1, 2, 1], this means you have 5 sandwiches to give out.
You can distribute them in the following order to the people: 2, 0, 1, 0.
Giving these sandwiches to the people their hunger levels now become: [1, 1, 1, 1].
The difference between each pair of people is now 0, the total is also 0, so your program should return 0.
Note: You may not have to give out all, or even any, of your sandwiches to produce a minimized difference.

Another example: if arr is [4, 5, 2, 3, 1, 0] then you can distribute the sandwiches in the following order: [3, 0, 1, 0, 0] which makes all the hunger levels the following: [2, 2, 2, 1, 0].
The differences between each pair of people is now: 0, 0, 1, 1 and so your program should return the final minimized difference of 2.

Examples:
Input: [5, 2, 3, 4, 5]
Output: 1

Input: [3, 2, 1, 0, 4, 1, 0]
Output: 4
"""

def FoodDistribution(arr):
  sandwiches = arr[0]
  hunger = arr[1:]
  n = len(hunger)
  memo = {}

  def total_diff(h):
    return sum(abs(h[i] - h[i+1]) for i in range(n-1))

  def dfs(idx, h_tuple, remaining):
    if idx == n or remaining == 0:
      return total_diff(h_tuple)

    key = (idx, h_tuple, remaining)
    if key in memo:
      return memo[key]

    best = float('inf')
    # try giving 0..remaining sandwiches to this person
    for give in range(remaining+1):
      new_h = list(h_tuple)
      new_h[idx] = max(0, new_h[idx] - give)
      best = min(best, dfs(idx+1, tuple(new_h), remaining-give))

    memo[key] = best
    return best

  return dfs(0, tuple(hunger), sandwiches)

# keep this function call here
# print(FoodDistribution(input()))

# Testing:
arr1 = [5, 2, 3, 4, 5] # 1
arr2 = [3, 2, 1, 0, 4, 1, 0] # 4
arr3 = [5, 3, 1, 2, 1] # 0
arr4 = [4, 5, 2, 3, 1, 0] # 2

print(FoodDistribution(arr1))
print(FoodDistribution(arr2))
print(FoodDistribution(arr3))
print(FoodDistribution(arr4))