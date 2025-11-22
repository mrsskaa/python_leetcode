class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j1 = m-1
        j2 = n-1

        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]

        else:
            for i in range(m+n-1, -1, -1):
                if j2 < 0:
                    break

                elif j1 < 0 and j2 >= 0:
                    nums1[i] = nums2[j2]
                    j2 -= 1

                elif  nums1[j1] <= nums2[j2]:
                    nums1[i] = nums2[j2]
                    j2 -= 1

                else:
                    nums1[i] = nums1[j1]
                    j1 -= 1

        return nums1



