"""
You are given a table, in which every key is a stringified number, and each corresponding value is an array of characters
e.g.
{
  "1": ["A", "B", "C"],
  "2": ["A", "B", "D", "A"],
}

Create a function that returns a table with the same keys, but each character should appear only once among the value-arrays
e.g.
{
  "1": ["C"],
  "2": ["A", "B", "D"],
}

Rules
Whenever two keys share the same character, they should be compared numerically, and the larger key will keep that character.
That's why in the example above the array under the key "2" contains "A" and "B", as 2 > 1.
If duplicate characters are found in the same array, the first occurrence should be kept.

Example 1
input = {
  "1": ["C", "F", "G"],
  "2": ["A", "B", "C"],
  "3": ["A", "B", "D"],
}
output = {
  "1": ["F", "G"],
  "2": ["C"],
  "3": ["A", "B", "D"],
}

Example 2
input = {
  "1": ["A"],
  "2": ["A"],
  "3": ["A"],
}
output = {
  "1": [],
  "2": [],
  "3": ["A"],
}

Example 3
input = {
  "432": ["A", "A", "B", "D"],
  "53": ["L", "G", "B", "C"],
  "236": ["L", "A", "X", "G", "H", "X"],
  "11": ["P", "R", "S", "D"],
}
output = {
  "11": ["P", "R", "S"],
  "53": ["C"],
  "236": ["L", "X", "G", "H"],
  "432": ["A", "B", "D"],
}
"""

def remove_duplicate_ids(obj):
    output_table = {} # make a new table with each key containing no duplicates

    for key, value in obj.items(): # use .items() to extract from dict
        seen = set() # set is unordered but cannot contain duplicates
        new_list = [] # append to new list
        for char in value: # loop through the values
            if char not in seen:
                seen.add(char) # .add() for a set
                new_list.append(char) # .append() for a list
        output_table[key] = new_list # then loop through the keys and add the new_lists to the output_table

    # compare the keys sharing same values and get larger key to keep character
    char_owner = {} # tracks who owns the character
    sorted_keys = [str(k) for k in sorted(int(k) for k in output_table.keys())] # take a key, turn to into to sort, then turn back to string
    for key in sorted_keys:
        for char in output_table[key][:]: # from smallest to largest
            if char in char_owner:
                owner_key = char_owner[char]
                if int(key) > int(owner_key): # updates char_owner
                    output_table[owner_key].remove(char)
                    char_owner[char] = key
                else:
                    output_table[key].remove(char) # removes from current list and stop checking for this key
                    break
            else: # if not owner, mark key as owner
                char_owner[char] = key

    return output_table


print(remove_duplicate_ids({
  "1": ["C", "F", "G"],
  "2": ["A", "B", "C"],
  "3": ["A", "B", "D"],
}))

print(remove_duplicate_ids({
  "1": ["A"],
  "2": ["A"],
  "3": ["A"],
}))

print(remove_duplicate_ids({
  "432": ["A", "A", "B", "D"],
  "53": ["L", "G", "B", "C"],
  "236": ["L", "A", "X", "G", "H", "X"],
  "11": ["P", "R", "S", "D"],
}))