from collections import Counter
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        counts = Counter(nums1)
        res = []

        for i in nums2:
            if counts[i] > 0:
                res.append(i)
                counts[i] -= 1

        return res
