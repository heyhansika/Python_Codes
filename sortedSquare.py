class Solution:
    def sortedSquares(self, nums):

        n = len(nums)

        result = [0] * n

        left = 0
        right = n - 1

        pos = n - 1

        while left <= right:

            leftSquare = nums[left] * nums[left]
            rightSquare = nums[right] * nums[right]

            if leftSquare > rightSquare:
                result[pos] = leftSquare
                left += 1
            else:
                result[pos] = rightSquare
                right -= 1

            pos -= 1

        return result
