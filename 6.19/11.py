from typing import List
nums=[1,1,2,2,4,5,6,6]
# for i in nums:
#     n=nums.index(i)+1
#     m=len(nums)
#     while n<m:
#         if nums[n]==i:
#             nums[n]=None
#             n+=1
#         else:
#             n+=1
# count=0
# for i in nums:
#     if i ==None:
#         continue
#     count+=1


# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         n=len(set(nums))
#         i=0
#         while i<n-1:
#             if nums[i]==nums[i+1]:
#                 temp=nums[i]
#                 nums[i+1:len(nums)-1]=nums[i+2:]
#                 nums[-1]=temp
#                 continue
#             else:
#                 i+=1
#         return i


slow=0
fast=1
while fast<len(nums):
    if nums[fast]==nums[slow]:
        fast+=1
    else:
        slow+=1
        nums[slow]=nums[fast]
        fast+=1
print(nums)









