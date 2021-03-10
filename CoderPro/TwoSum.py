#given an array of numbers and a target number, target number is sum of 2 unique numbers
#return the two indices of the numbers that equal the target number

class Solution(object):
    def twoSum(self, nums, target):
        values = {}
        for i, num in enumerate(nums):
            diff = target - num 
            if diff in values:
                return [i, values[diff]]
            values[num] = 1
        return []

print(Solution().twoSum([2, 7, 11, 15], 18))