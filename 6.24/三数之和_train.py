def threeSum(nums):
    nums.sort()
    res=[]
    for i in range(len(nums)-2):
        if nums[i+1]==nums[i] and i>0:
            continue
        left=i+1
        right=len(nums)-1
        while left<right:
            sum=nums[i]+nums[left]+nums[right]
            if sum>0:
                right-=1
            elif sum<0:
                left+=1
            else:
                res.append([nums[i],nums[left],nums[right]])
                while left<right and nums[left+1]==nums[left]:
                    left+=1
                while left<right and nums[right]==nums[right-1]:
                    right-=1
                left+=1
                right-=1
    return res
n=threeSum([-1,0,0,1,1])
print(n)