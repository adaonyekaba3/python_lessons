"""
Unpacking
The biggest advantage of using Python for coding interviews is its simplicity and readability.
In this section we will learn some of the shortcuts Python provides to make our code easy to read and write.

One of these shortcuts is unpacking.

point1 = [0, 0]
point2 = [2, 4]

x1, y1 = point1 # x1 = 0, y1 = 0
x2, y2 = point2 # x2 = 2, y2 = 4

slope = (y2 - y1) / (x2 - x1)

print(slope) # Output: 2.0
Above, we have code that calculates the slope of a line given two points.
Each point is a list of two integers.
Notice how we have two variables on the left side of the assignment operator, with a list on the right side. This is called unpacking. We know point1 and point2 are lists of size 2, so we can unpack them into two variables each.
The below code accomplishes the same without unpacking but with slightly more code:

x1, y1 = point1[0], point1[1]
x2, y2 = point2[0], point2[1]
If we attempt unpacking with not enough variables on the left-side, we will get a ValueError.

x, y = [0, 0, 0] # ValueError: too many values to unpack (expected 2)
Unpacking also works with tuples and sets with the same syntax.

Challenge
Implement the following functions using unpacking:

sum_3_integers(triplet: List[int]) -> int that takes a list of 3 integers and returns the sum of the integers.
compute_volume(box_dimensions: Tuple[int, int, int]) -> int that takes a list of 3 integers representing [width, height, depth] of a box and returns the volume of it.
"""

from typing import List, Tuple

"""sum_3_integers(triplet: List[int]) -> int that takes a list of 3 integers and returns the sum of the integers.
 """
def sum_3_integers(triplet: List[int]) -> int:
    sum = 0
    # loop over each item in list
    for item in triplet:
        # add item to sum
        sum += item
        # print(f"Adding {item} to sum, current sum is {sum}")
    return sum
    # return sum(triplet)


"""
compute_volume(box_dimensions: Tuple[int, int, int]) ->
int that takes a list of 3 integers representing [width, height, depth] of a box and returns the volume of it.
"""
def compute_volume(box_dimensions: Tuple[int, int, int]) -> int:
    volume = 1
    for item in box_dimensions:
        # print(f"Adding {item} to volume, current volume is {volume}")
        volume *= item
    # print(f"Multiplying {item} to volume, current volume is {volume}")
    return volume


# do not modify below this line
print(sum_3_integers([1, 2, 3]))
print(sum_3_integers([4, 6, 2]))

print(compute_volume((1, 2, 3)))
print(compute_volume((3, 2, 1)))
print(compute_volume((3, 9, 7)))
