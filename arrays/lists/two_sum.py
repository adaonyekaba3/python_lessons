"""
1. Two Sum
Easy
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order. 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.


Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""
""" class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_to_index = {}
        for index, num in enumerate(nums):
            complement = target - num
            print(f"Index: {index}, Num: {num}, Complement: {complement}, Num to Index Map: {num_to_index}")
            if complement in num_to_index:
                return [num_to_index[complement], index]
            num_to_index[num] = index
        return [] """

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create an empty hashmap to store returned indices
        hmap_result = {} # val : index

        for i, n in enumerate(nums):
            diff_to_target = target - n
            if diff_to_target in hmap_result:
                return [hmap_result[diff_to_target], i]
            hmap_result[n] = i
        return

two_sum = Solution().twoSum([2, 7, 11, 15], 9)
print(two_sum)  # Output: [0, 1] 