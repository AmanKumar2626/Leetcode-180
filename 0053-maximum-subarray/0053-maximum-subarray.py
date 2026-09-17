class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        sum = nums[0]
        maxsum = nums[0]
        for i in range(1, len(nums)):
            sum = max(nums[i], nums[i] + sum)
            maxsum = max(sum, maxsum)

        return maxsum
                