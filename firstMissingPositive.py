class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)

        # Place each number at its correct index
        for i in range(n):
            while (
                nums[i] > 0 and
                nums[i] <= n and
                nums[nums[i] - 1] != nums[i]
            ):
                correct_index = nums[i] - 1

                nums[i], nums[correct_index] = (
                    nums[correct_index],
                    nums[i]
                )

        # Find first missing positive
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1
