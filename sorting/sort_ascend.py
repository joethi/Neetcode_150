def sort_asc(nums):
    nums_len = len(nums)
    for i in range(nums_len-1):
        for j in range(nums_len-i-1):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
        
    return nums

nums = [2,5,1,4,3,0]
nums = [-9,8,5,70,4,3,3,100]
print(sort_asc(nums))