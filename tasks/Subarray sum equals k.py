class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        prefix = []
        sum = 0
        cnt = 0
        prefix_cnt = {0:1}

        for i in nums:
            sum += i
            prefix.append(sum)

        for i in range(len(prefix)):
            if prefix[i] - k in prefix_cnt:
                cnt += prefix_cnt[prefix[i] - k]

            if prefix[i] in prefix_cnt:
                prefix_cnt[prefix[i]] += 1
            else:
                prefix_cnt[prefix[i]] = 1

        return cnt
