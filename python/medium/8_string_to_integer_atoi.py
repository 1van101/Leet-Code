class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        max_int = 2 ** 31 - 1
        min_int = -2 ** 31
        if not s:
            return 0

        start_i = 0
        sign = 1

        if s[0] in ('-', '+'):
            start_i += 1
            sign = -1 if s[0] == '-' else 1

        res = ''

        for i in range(start_i, len(s)):
            if s[i].isdigit():
                res += s[i]
            else:
                break

        if res:
            res = int(res) * sign
            if min_int <= res <= max_int:
                return res
            else:
                return min_int if res < min_int else max_int
        return 0