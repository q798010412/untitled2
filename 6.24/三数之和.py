def three_sum(nums):
    nums.sort()
    result=[]
    for i in range(len(nums)):
        left=i+1
        right=len(nums)-1
        temp=nums[i]+nums[left]+nums[right]
        while left<right:
            if temp==0:
                result.append([nums[i],nums[left],nums[right]])
            else:
                if temp>0:
                    right-=1
                else:
                    left+=1
    return result