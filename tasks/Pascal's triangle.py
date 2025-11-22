class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 0:
            return []

        if numRows == 1:
            return [[1]]

        a = [[1]]


        for i in range(1, numRows):
            b = [1]
            for j in range(1, i):
                b.append(a[-1][j - 1] + a[-1][j])
            b.append(1)
            a.append(b)

        return a
