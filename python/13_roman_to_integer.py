class Solution:
    def romanToInt(self, s: str) -> int:

        symbols = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0

        for i in range(len(s)):
            current_num = symbols[s[i]]

            if i == len(s) - 1:
                return result + current_num

            next_num = symbols[s[i + 1]]

            if next_num > current_num:
                result -= current_num
            else:
                result += current_num

