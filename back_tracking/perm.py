def permute(nums):
    #write code here   
    res = []
    def perm(i):
        if i == (len(nums) - 1):
            res.append(nums[:])
            return
        for j in range(i,len(nums)):
            nums[j], nums[i] = nums[i], nums[j]
            perm(i+1)
            nums[j], nums[i] = nums[i], nums[j]
        # return res
    perm(0)
    return res

nums = [1]    
print(permute(nums))    