from typing import List


def remove_zero(nums: List[int]) -> List:
    slow = 0
    fast = 0
    while fast < len(nums):
        if nums[fast] == 0:
            fast += 1
        else:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
            fast += 1
    return nums


n = remove_zero([0, 1, 0, 3, 1, 0, 2, 0])
print(n)
