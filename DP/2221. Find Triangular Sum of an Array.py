class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            print(nums[0])
        else:
            for j in range(len(nums)-1):
                l=nums[:-1]
                for i in range(len(nums)-1):
                    l[i] = nums[i]+nums[i+1]
                    if nums[i] + nums[i + 1] >= 10:
                        l[i] -= 10
                nums=l
            print(l[0])

Solution().triangularSum([5])