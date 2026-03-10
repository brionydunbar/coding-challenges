"""
Have the function WordSplit(strArr) read the array of strings stored in strArr, which will contain 2 elements: the first element will be a sequence of characters, and the second element will be a long string of comma-separated words, in alphabetical order, that represents a dictionary of some arbitrary length.
For example: strArr can be: ["hellocat", "apple,bat,cat,goodbye,hello,yellow,why"].
Your goal is to determine if the first element in the input can be split into two words, where both words exist in the dictionary that is provided in the second input.
In this example, the first element can be split into two words: hello and cat because both of those words are in the dictionary.

Your program should return the two words that exist in the dictionary separated by a comma.
So for the example above, your program should return hello,cat.
There will only be one correct way to split the first element of characters into two words.
If there is no way to split string into two words that exist in the dictionary, return the string not possible.
The first element itself will never exist in the dictionary as a real word.

Examples:
Input: ["baseball", "a,all,b,ball,bas,base,cat,code,d,e,quit,z"]
Output: base,ball

Input: ["abcgefd", "a,ab,abc,abcg,b,c,dog,e,efd,zzzz"]
Output: abcg,efd
"""

def WordSplit(strArr):
  for i, j in enumerate(strArr[1].split(",")): # split comma separated words into list
    # subtract a string from main string
    new = strArr[0].replace(j.strip(),"")
    # search through other strings and compare
    for word in strArr[1].split(","):
      if new == word.strip(): # check if the new word from first string is same as anything in list
        if strArr[0] == j.strip() + new: # check if match
          return f"{j.strip()},{new}"
  return "not possible"

# keep this function call here
# print(WordSplit(input()))

# Testing:
arr1 = ["baseball", "a,all,b,ball,bas,base,cat,code,d,e,quit,z"] # "base,ball"
arr2 = ["abcgefd", "a,ab,abc,abcg,b,c,dog,e,efd,zzzz"] # "abcg,efd"
arr3 = ["hellocat", "apple,bat,cat,goodbye,hello,yellow,why"] # "hello,cat"

print(WordSplit(arr1))
print(WordSplit(arr2))
print(WordSplit(arr3))