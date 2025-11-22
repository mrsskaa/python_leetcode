class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = set(nums)
        ans = 0
        for i in nums:
            if i-1 not in nums:
                j = i+1
                while j in nums:
                    j += 1
                ans = max(ans, j-i)

        return ans
