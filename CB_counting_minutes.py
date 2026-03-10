"""
Have the function CountingMinutes(str) take the str parameter being passed which will be two times (each properly formatted with a colon and am or pm) separated by a hyphen and return the total number of minutes between the two times.
The time will be in a 12 hour clock format.
For example: if str is 9:00am-10:00am then the output should be 60.
If str is 1:00pm-11:00am the output should be 1320.

Examples:
Input: "12:30pm-12:00am"
Output: 690

Input: "1:23am-1:08am"
Output: 1425
"""

from datetime import datetime, timedelta

def CountingMinutes(strParam):
  # split string
  start_str, end_str = strParam.split("-")
  # change times to datetime format
  t1 = datetime.strptime(start_str, "%I:%M%p")
  t2 = datetime.strptime(end_str, "%I:%M%p")
  # get difference
  if t2 <= t1:
    t2 += timedelta(days = 1)
  delta = t2 - t1
  result = int(delta.total_seconds() // 60)
  return result

# keep this function call here
# print(CountingMinutes(input()))


# Testing
str1 = "12:30pm-12:00am" # 690
str2 = "1:23am-1:08am" # 1425
str3 = "9:00am-10:00am" # 60
str4 = "1:00pm-11:00am" # 1320

print(CountingMinutes(str1))
print(CountingMinutes(str2))
print(CountingMinutes(str3))
print(CountingMinutes(str4))