class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        t = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[t] = nums[i]
                t += 1
        return t
