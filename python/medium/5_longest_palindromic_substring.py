class Solution:
    def longestPalindrome(self, s: str) -> str:

        palindromic_substring = ''

        for i in range(len(s)):
            for j in range(i, len(s) + 1):
                current_substr = s[i:j:1]

                if current_substr == current_substr[::-1] and len(current_substr) > len(palindromic_substring):
                    palindromic_substring = current_substr

        return palindromic_substring






