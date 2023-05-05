class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s) // 2):
            i_to_change = len(s) - i - 1
            s[i], s[i_to_change] = s[i_to_change], s[i]