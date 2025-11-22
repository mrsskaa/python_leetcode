class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1 or n == 7:
            return True
        elif n<10:
            return False
        else:
            s = str(n)
            n = 0
            for i in s:
                n += int(i)**2

            return self.isHappy(n)
