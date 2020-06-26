# def two_sum(nums,target):
#     nums.sort(reverse=False)
#     left=0
#     right=len(nums)-1
#     print(nums)
#     while left<right:
#         if nums[left]+nums[right]==target:
#             return nums[left], nums[right]
#
#             left+=1
#             right-=1
#         else:
#             if nums[left]+nums[right]<target:
#                 left+=1
#             else:
#                 right-=1
# print(two_sum([1,2,3,4,5,8,6],6))

def two_sum(nums,target):
    temp_list={}
