from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = Counter(s)
        ans = 10**10


        for i in d:
            if d[i] == 1:
                ans = min(s.find(i), ans)

        if ans == 10**10:
            return -1

        return ans


solution = Solution()

print(solution.firstUniqChar("loveleetcode"))