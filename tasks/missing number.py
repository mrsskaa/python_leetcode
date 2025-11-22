class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        a = [-1] * (n + 1)
        for i in nums:
            a[i] = i

        for i in range(len(a)):
            if a[i] == -1:
                return i

        return 0