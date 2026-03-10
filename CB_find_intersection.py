"""
Have the function FindIntersection(strArr) read the array of strings stored in strArr which will contain 2 elements: the first element will represent a list of comma-separated numbers sorted in ascending order, the second element will represent a second list of comma-separated numbers (also sorted). Your goal is to return a comma-separated string containing the numbers that occur in elements of strArr in sorted order. If there is no intersection, return the string false.
Examples
Input: ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
Output: 1,4,13
Input: ["1, 3, 9, 10, 17, 18", "1, 4, 9, 10"]
Output: 1,9,10
"""

def FindIntersection(strArr):

    # split the strings into arrays
    list1 = strArr[0].split(",")
    list1 = [x.strip(" ") for x in list1]
    list2 = strArr[1].split(",")
    list2 = [x.strip(" ") for x in list2]

    intersection = [] #initialise an array to store the intersecting values
    for i in list1:
        if i in list2:
            intersection.append(i) # add to the array
        else:
            continue
    if len(intersection) == 0:
        return "false"
    else: # make the string
        intersection_string = ",".join(intersection)
        return intersection_string

print(FindIntersection(["1, 5, 6, 7, 10, 11, 12", "5, 6, 8, 11, 17"]))
print(FindIntersection(["2, 3, 4", "3"]))
print(FindIntersection(["1, 2, 4, 5, 6, 9", "2, 3, 4, 8, 10"]))