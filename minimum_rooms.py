"""
This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""

def minimum_rooms(intervals):
    
    starting_times = [x[0] for x in intervals]
    ending_times = [x[1] for x in intervals]

    starting_times.sort()
    ending_times.sort()

    rooms = 0
    curr_rooms = 0
    start_index = 0
    end_index = 0

    while start_index < len(starting_times) and end_index < len(ending_times):
        
        if starting_times[start_index] < ending_times[end_index]:
            curr_rooms += 1
            start_index += 1
        else:
            curr_rooms -= 1
            end_index += 1
        rooms = max(rooms, curr_rooms)

    return rooms

intervals = [(30, 75), (0, 50), (60, 150)]
assert minimum_rooms(intervals) == 2

intervals = [(5, 7), (0, 9), (5, 9)]
assert minimum_rooms(intervals) == 3

intervals = [(10,15),(10,15)]
assert minimum_rooms(intervals) == 2

intervals = [(10,20), (15,25), (25,30), (20,30)]
assert minimum_rooms(intervals) == 2