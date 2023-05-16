import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        matches = re.findall(p, s)

        if matches:
            return True if len(matches[0]) == len(s) else False

        return False