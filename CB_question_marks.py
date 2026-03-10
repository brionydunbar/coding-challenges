"""
Have the function QuestionsMarks(str) take the str string parameter, which will contain single digit numbers, letters, and question marks,
and check if there are exactly 3 question marks between every pair of two numbers that add up to 10.
If so, then your program should return the string true, otherwise it should return the string false.
If there aren't any two numbers that add up to 10 in the string, then your program should return false as well.

For example: if str is "arrb6???4xxbl5???eee5" then your program should return true
because there are exactly 3 question marks between 6 and 4, and 3 question marks between 5 and 5 at the end of the string.
"""

def QuestionsMarks(strParam):
    found_valid_pair = False

    for i in range(len(strParam)):
        if strParam[i].isdigit():
            num1 = int(strParam[i])
            q_count = 0

            for j in range(i+1, len(strParam)):
                if strParam[j] == "?":
                    q_count += 1
                elif strParam[j].isdigit():
                    num2 = int(strParam[j])
                    if num1 + num2 == 10:
                        if q_count == 3:
                            found_valid_pair = True
                        else:
                            return False

                    q_count = 0

    if found_valid_pair:
        return "true"
    else:
        return "false"

print(QuestionsMarks("arrb6???4xxbl5???eee5"))
print(QuestionsMarks("aa6?9"))