from typing import List, Any
def remove(nums: List[Any], val: Any) -> int:
    slow = 0
    fast = 0
    while fast < len(nums):
        if nums[fast] == val:
            fast += 1
        else:
            nums[slow] = nums[fast]
            slow += 1
            fast += 1
    return slow


a = remove([1, 2, 2, 1, 3, 3, 4, ], 2)
print(a)
