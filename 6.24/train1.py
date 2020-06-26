def remove_var(nums,var):
    slow=0
    fast=0
    while fast<len(nums):
        if nums[fast]==var:
            fast+=1
        else:
            nums[slow]=nums[fast]
            fast+=1
            slow+=1
    return slow,nums
a=remove_var([1,2,3,3,4],3)
print(a)