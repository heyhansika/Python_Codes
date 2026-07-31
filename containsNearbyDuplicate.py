class Solution:
    def containsNearbyDuplicate(self, nums, k):

        indexMap = {}

        for i in range(len(nums)):

            if nums[i] in indexMap and i - indexMap[nums[i]] <= k:
                return True

            indexMap[nums[i]] = i

        return False
