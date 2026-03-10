"""
- Tandem bicycle is operated by two people: rider A and rider B. Both riders pedal, but the rider who pedals faster dictates the speed of the bicycle
- If rider A goes at a speed of 10 and rider B pedals at a speed of 8, the bicycle will be moving at a speed of 10: tandem_speed = max(speed_A, speed_B)
- You are given two lists of integers. Both lists have the same length. First list represent speeds of riders who wear blue shirts and list two represents speeds of riders in red shirts. The number of blue riders equals the number of red riders
- Each bicycle needs to be ridden by two people: one in red and the other one in blue shirt!

Goal

- Pair every rider wearing a red shirt with a rider wearing a blue shirt to operate a tandem bike
- Write a function that returns the maximum possible OR the minimum possible TOTAL SPEED of ALL TANDEMS being ridden
- The indication of max or min speed will be based on an input param ‘fastest’. If ‘fastest = true’, then return max total speed or vice-versa

Total speed example:*
- Total speed is the sum of the speeds of all tandems being ridden
- If we have 4 riders: (2 blue, 2 red) who have speeds 1,2,3,4 and they are paired as [1, 3] & [4,2] then total speed will be: 3 + 4 = 7
"""

def tandem_speed(red_speeds, blue_speeds, fastest):
    # Sort both lists to ake it easier to decide how to pair
    red_speeds.sort()
    blue_speeds.sort()

    # If fastest, reverse one list to maximize pairing
    if fastest:
        blue_speeds.reverse()

    # fastest - pair slowest red with fastest blue
    # slowest - pair slowest red with slowest blue

    total_speed = 0  # add the total speed of each tandem
    for r, b in zip(red_speeds, blue_speeds):  # zip to get pairings
        total_speed += max(r, b)  # calculate max of each pair

    return total_speed

#############################################################

# Test Case 1 -- result 32

red_speeds = [5, 5, 3, 9, 2]
blue_speeds = [3, 6, 7, 2, 1]
fastest = True
#
print(tandem_speed(red_speeds, blue_speeds, fastest))


#############################################################

# Test Case 2 -- result 25

red_speeds = [5, 5, 3, 9, 2]
blue_speeds = [3, 6, 7, 2, 1]
fastest = False
#
print(tandem_speed(red_speeds, blue_speeds, fastest))

#############################################################

# Test Case 3 -- result 30

red_speeds = [1, 2, 1, 9, 12, 3]
blue_speeds = [3, 3, 4, 6, 1, 2]
fastest = False
#
print(tandem_speed(red_speeds, blue_speeds, fastest))

#############################################################

# Test Case 4 -- result 37
#
red_speeds = [1, 2, 1, 9, 12, 3]
blue_speeds = [3, 3, 4, 6, 1, 2]
fastest = True
#
print(tandem_speed(red_speeds, blue_speeds, fastest))