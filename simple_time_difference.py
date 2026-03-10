"""
In this Kata, you will be given a series of times at which an alarm sounds.
Your task will be to determine the maximum time interval between alarms.
Each alarm starts ringing at the beginning of the corresponding minute and rings for exactly one minute.
The times in the array are not in chronological order. Ignore duplicate times, if any.

For example:
solve(["14:51"]) = "23:59".
If the alarm sounds now, it will not sound for another 23 hours and 59 minutes.

solve(["23:00","04:22","18:05","06:24"]) == "11:40".
The max interval that the alarm will not sound is 11 hours and 40 minutes.
In the second example, the alarm sounds 4 times in a day.
"""

import datetime
from datetime import datetime

def solve(arr):
    if len(arr) == 1:
        return "23:59"

    # parse times into minutes since midnight
    unique_mins_set = set()

    for time in arr:
        h, m = time.split(":")
        total_mins = int(h) * 60 + int(m)
        unique_mins_set.add(total_mins)

    unique_mins = sorted(unique_mins_set)

    max_gap = 0

    # check for gaps between consecutive times
    for i in range(1, len(unique_mins)):
        gap = unique_mins[i] - unique_mins[i-1]
        max_gap = max(max_gap, gap)

    # check wrap-around gap (next day)
    wrap_gap = (24 * 60 - unique_mins[-1] + unique_mins[0])
    max_gap = max(max_gap, wrap_gap)
    max_gap -= 1 # account for ringing for 1 min

    # format result
    hours = max_gap // 60
    minutes = max_gap % 60
    return f"{hours:02}:{minutes:02}"


print(solve(["14:51"]))
print(solve(["23:00","04:22","18:05","06:24"]))
print(solve(["21:14", "15:34", "14:51", "06:25", "15:30"]))