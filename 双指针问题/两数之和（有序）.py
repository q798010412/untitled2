from typing import List


def twoSum(nums: List[int], target: int) -> tuple:
    left = 0
    right = len(nums) - 1
    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            return left, right
        else:
            if sum > target:
                right -= 1
            else:
                left += 1


a = twoSum([2, 7, 11, 15], 9)
print(a)
