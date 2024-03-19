class Solution(object):
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
        nums.append(target)
        nums = sorted(nums)
        return nums.index(target)
