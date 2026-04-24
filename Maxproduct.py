class Solution:
    def maxProduct(self, nums):
        max_prod = nums[0]
        min_prod = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            curr = nums[i]

            # If negative, swap max and min
            if curr < 0:
                max_prod, min_prod = min_prod, max_prod

            max_prod = max(curr, max_prod * curr)
            min_prod = min(curr, min_prod * curr)

            ans = max(ans, max_prod)

        return ans
