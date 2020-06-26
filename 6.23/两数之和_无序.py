def two_sum(nums,target):
    target_dict={}
    for i in range(len(nums)):
        temp=target-nums[i]
        if temp in target_dict:
            return target_dict[temp],i
        else:
            target_dict[nums[i]]=i
print(two_sum([1,4,5,6,7,8,2],3))