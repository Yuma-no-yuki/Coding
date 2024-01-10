class Solution(object):
    def triangularSum(self, nums):
        if len(nums) == 1:
            return nums[0]
        else:
            for j in range(len(nums)-1):
                l=nums[:-1]
                for i in range(len(nums)-1):
                    l[i] = nums[i]+nums[i+1]
                    if nums[i] + nums[i + 1] >= 10:
                        l[i] -= 10
                nums=l
            return l[0]
