# 删除指定元素
# nums=[3,2,2,3,3,3,2]
# slow=0
# fast=0
# val=3
# while fast<len(nums):
#     if nums[fast]==val:
#         fast+=1
#     else:
#         nums[slow]=nums[fast]
#         slow+=1
#         fast+=1
# print(nums)
# print(slow)

# 移动0
# nums=[0,1,0,3,12]
# fast=0
# slow=0
# while fast<len(nums):
#     if nums[fast]==0:
#         fast+=1
#     else:
#         nums[slow],nums[fast]=nums[fast],nums[slow]
#         slow+=1
#         fast+=1
# print(nums)

# 最多重复2次
nums=[1,1,1,2,2,3,3,3]
a=2
for i in range(2,len(nums)):
    if nums[i]!=nums[a-2]:
        nums[a]=nums[i]



print(nums)

