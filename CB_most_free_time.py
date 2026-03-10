"""
Have the function MostFreeTime(strArr) read the strArr parameter being passed which will represent a full day and will be filled with events that span from time X to time Y in the day.
The format of each event will be hh:mmAM/PM-hh:mmAM/PM.
For example, strArr may be ["10:00AM-12:30PM","02:00PM-02:45PM","09:10AM-09:50AM"].
Your program will have to output the longest amount of free time available between the start of your first event and the end of your last event in the format: hh:mm.
The start event should be the earliest event in the day and the latest event should be the latest event in the day.
The output for the previous input would therefore be 01:30 (with the earliest event in the day starting at 09:10AM and the latest event ending at 02:45PM).
The input will contain at least 3 events and the events may be out of order.

Examples:
Input: ["12:15PM-02:00PM","09:00AM-10:00AM","10:30AM-12:00PM"]
Output: 00:30

Input: ["12:15PM-02:00PM","09:00AM-12:11PM","02:02PM-04:00PM"]
Output: 00:04
"""

from datetime import datetime


def MostFreeTime(strArr):
  # helper to convert times to minutes
  def _to_minutes(time):
    dt = datetime.strptime(time, "%I:%M%p")
    return dt.hour * 60 + dt.minute

  # parse into (start_min, end_min)
  intervals = []
  for event in strArr:
    start_s, end_s = event.split("-")
    intervals.append((_to_minutes(start_s), _to_minutes(end_s)))

  # sort by start time
  intervals.sort()

  # merge overlapping/contiguous intervals
  merged = []
  for start, end in intervals:
    if not merged or start > merged[-1][1]:
      merged.append([start, end])
    else:
      if end > merged[-1][1]:
        merged[-1][1] = end

  # find maximum gap between merged intervals
  max_gap = 0
  for i in range(len(merged) - 1):
    gap = merged[i + 1][0] - merged[i][1]
    if gap > max_gap:
      max_gap = gap

  hours = max_gap // 60
  minutes = max_gap % 60
  return f"{hours:02d}:{minutes:02d}"

# keep this function call here
# print(MostFreeTime(input()))

# Testing:
arr1 = ["12:15PM-02:00PM","09:00AM-10:00AM","10:30AM-12:00PM"] # "00:30"
arr2 = ["12:15PM-02:00PM","09:00AM-12:11PM","02:02PM-04:00PM"] # "00:04"
arr3 = ["10:00AM-12:30PM","02:00PM-02:45PM","09:10AM-09:50AM"] # "01:30"

print(MostFreeTime(arr1))
print(MostFreeTime(arr2))
print(MostFreeTime(arr3))