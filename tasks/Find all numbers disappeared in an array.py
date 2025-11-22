class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        ans = []
        for i in range(len(nums)):
            x = abs(nums[i]) - 1
            nums[x] = - abs(nums[x])

        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i+1)
        return ans
