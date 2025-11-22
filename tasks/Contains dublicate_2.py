class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        if len(nums) == len(set(nums)):
            return False

        elif len(nums) <= k:
            return True

        else:
            for i in range(len(nums)):
                for j in range(i+1, i+k+1):
                    if nums[i] == nums[j]:
                        return True

            return False