"""
When users post an update on social media,such as a URL, image, status update etc., other users in their network are able to view this new post on their news feed.
Users can also see exactly when the post was published, i.e, how many hours, minutes or seconds ago.

Since sometimes posts are published and viewed in different time zones, this can be confusing.
You are given two timestamps of one such post that a user can see on his newsfeed in the following format:

Day dd Mon yyyy hh:mm:ss +xxxx

Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.

Input Format
The first line contains T, the number of testcases.
Each testcase contains 2 lines, representing time t1 and time t2.


Output Format
Print the absolute difference (t1 - t2) in seconds.

Sample Input
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000

Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000

Sample Output
25200

88200

Explanation
In the first query, when we compare the time in UTC for both the time stamps, we see a difference of 7 hours. which is 7 x 3600 seconds or 25200 seconds
Similarly, in the second query, time difference is 5 hours and 30 minutes for time zone adjusting for that we have a difference of 1 day and 30 minutes.
Or 24 x 3600 + 30 x 60 = 88200
"""


from datetime import datetime

def time_delta(t1, t2):
    t1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    t2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    difference = abs(int((t1 -t2).total_seconds()))

    return difference

print(time_delta("Sun 10 May 2015 13:54:36 -0700", "Sun 10 May 2015 13:54:36 -0000"))