from typing import List


def threeSum(nums: List[int]) -> List:
    nums.sort()
    res = []
    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        sum = nums[i] + nums[left] + nums[right]
        while left < right:
            if sum > 0:
                right -= 1
            elif sum < 0:
                left += 1
            else:
                res.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left + 1] == nums[right]:
                    left += 1
                while left < right and nums[right - 1] == nums[right]:
                    right -= 1
                left += 1
                right -= 1
    return res


a = threeSum([-1, 0, 1, 2, -1, -4])
print(a)
