#given an array nums. We define a running sum of an array as runningSum[i]  = sum(num[0]..num[i])
#return the running sum of nums
#https://leetcode.com/problems/running-sum-of-1d-array/

from typing import List


def runningSum(nums):
    for item in range(1, len(nums)):
        nums[item] = nums[item - 1] + nums[item]
    return nums

if __name__ == '__main__':
    nums = [1,2,3,4]
    #print(type(newList))
    print(runningSum(nums))
