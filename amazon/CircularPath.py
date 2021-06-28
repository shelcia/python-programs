# Find the first circular tour that visits all petrol pumps

# Suppose there is a circle. There are n petrol pumps on that circle.
# You are given two sets of data.


# The amount of petrol that every petrol pump has.
# Distance from that petrol pump to the next petrol pump.
# Calculate the first point from where a truck will be able to complete the circle
# (The truck will stop at each petrol pump and it has infinite capacity).
# Expected time complexity is O(n). Assume for 1-litre petrol, the truck can go 1 unit of distance.
# For example, let there be 4 petrol pumps with amount of petrol and
# distance to next petrol pump value pairs as {4, 6}, {6, 5}, {7, 3} and {4, 5}.
# The first point from where the truck can make a circular tour is 2nd petrol pump.
# Output should be “start = 1” (index of 2nd petrol pump).


def printTour(arr, length):
    print(arr)

    start = 0

    surplus = 0
    deficit = 0

    for i in range(length):

        surplus += arr[i][0] - arr[i][1]

        if(surplus < 0):
            start = i + 1
            deficit += surplus
            surplus = 0

    return start if (surplus+deficit) > 0 else -1


arr = [[6, 4], [3, 6], [7, 3]]
start = printTour(arr, 3)
if start == -1:
    print("No Solution Possible !!!")
else:
    print("start = {}".format(start))
