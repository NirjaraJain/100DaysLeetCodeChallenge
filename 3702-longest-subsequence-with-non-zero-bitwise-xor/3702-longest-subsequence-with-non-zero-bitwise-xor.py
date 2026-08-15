class Solution:
    def longestSubsequence(self, nums: list[int]) -> int:
        tos = nz = 0

        for n in nums:
            nz |= n > 0
            tos ^= n

        return nz * (len(nums) - (not tos))