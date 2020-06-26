from typing import List


def remove_re(nums: List[int]) -> int:
    slow = 0
    fast = 1
    while fast < len(nums):
        if nums[fast] == nums[slow]:
            fast += 1
        else:
            slow += 1
            nums[slow] = nums[fast]
            fast += 1
    return slow + 1


print(remove_re([1, 2, 2, 3, 3]))
