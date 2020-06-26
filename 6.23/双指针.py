# 删除重复值
def delete(nums):
    slow = 0
    fast = 1
    while fast < len(nums):
        if nums[fast] == nums[slow]:
            fast += 1
        else:
            slow += 1
            nums[slow] = nums[fast]
            fast += 1
    return slow + 1, nums


# if __name__ == '__main__':
#     n = delete([1, 1, 2, 2, 3, 3, 5, 5, 6, 6, 7, 7])
#     print(n)


# 删除指定值
def delete_1(nums,data):
    slow=0
    fast=0
    while fast < len(nums):
        if nums[fast]==data:
            fast+=1
        else:
            nums[slow]=nums[fast]
            slow+=1
            fast+=1
    return slow,nums
if __name__ == '__main__':
    n=delete_1([1,2,3,4,4,2],2)
    print(n)