class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        for i in range(20):
            if 3 ** i == n:
                return True
        return False


        # --with loop--
        # while n != 1:
        #     n /= 3
        #     if n % 1 != 0 or n == 0:
        #         return False
        # return True



