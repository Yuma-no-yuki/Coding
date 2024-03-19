class Solution(object):
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
        nums.append(target)
        nums = sorted(nums)
        return nums.index(target)

print(Solution().searchInsert([1,3,5,6],2))