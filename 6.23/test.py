# 去除重复值
# nums=[1,1,1,2,2,2,3,5,5,2,2]
# slow=0
# fast=1
# while fast < len(nums):
#     if nums[fast]==nums[slow]:
#         fast+=1
#     else:
#         slow+=1
#         nums[slow]=nums[fast]
#         fast+=1
# print(nums,slow+1)
a=[1,2,3]
a.append(4)
print(a)