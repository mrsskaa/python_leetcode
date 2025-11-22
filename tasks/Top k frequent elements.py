from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        d = Counter(nums)
        return list(dict(sorted(d.items(), key=lambda item: item[1], reverse=True)).keys())[:k]
