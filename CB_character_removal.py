"""
Have the function CharacterRemoval(strArr) read the array of strings stored in strArr, which will contain 2 elements: the first element will be a sequence of characters representing a word, and the second element will be a long string of comma-separated words, in alphabetical order, that represents a dictionary of some arbitrary length.
For example: strArr can be: ["worlcde", "apple,bat,cat,goodbye,hello,yellow,why,world"].
Your goal is to determine the minimum number of characters, if any, can be removed from the word so that it matches one of the words from the dictionary.
In this case, your program should return 2 because once you remove the characters "c" and "e" you are left with "world" and that exists within the dictionary.
If the word cannot be found no matter what characters are removed, return -1.

Examples:
Input: ["baseball", "a,all,b,ball,bas,base,cat,code,d,e,quit,z"]
Output: 4

Input: ["apbpleeeef", "a,ab,abc,abcg,b,c,dog,e,efd,zzzz"]
Output: 8

"""


def CharacterRemoval(strArr):
    target_word = strArr[0]
    dictionary_str = strArr[1]
    dictionary_words = set(dictionary_str.split(","))

    min_removed_count = float("inf")  # initialise with large number

    for word in dictionary_words:
        # check if word is subsequence of target word
        target_ptr = 0
        dict_ptr = 0
        while target_ptr < len(target_word) and dict_ptr < len(word):
            if target_word[target_ptr] == word[dict_ptr]:
                dict_ptr += 1
            target_ptr += 1

        # if word is subseq
        if dict_ptr == len(word):
            removed_count = len(target_word) - len(word)
            min_removed_count = min(min_removed_count, removed_count)

    return min_removed_count if min_removed_count != float("inf") else -1


# keep this function call here
# print(CharacterRemoval(input()))

# Testing:
arr1 = ["baseball", "a,all,b,ball,bas,base,cat,code,d,e,quit,z"]  # 4
arr2 = ["apbpleeeef", "a,ab,abc,abcg,b,c,dog,e,efd,zzzz"]  # 8
arr3 = ["worlcde", "apple,bat,cat,goodbye,hello,yellow,why,world"]  # 2

print(CharacterRemoval(arr1))
print(CharacterRemoval(arr2))
print(CharacterRemoval(arr3))