class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        results = []

        if len(s) == 1:
            return 1

        for i in range(len(s) - 1):
            substring = []
            substring.append(s[i])

            for j in range(i + 1, len(s)):
                current_char = s[j]

                if current_char not in substring:
                    substring.append(current_char)
                else:
                    results.append(len(substring))
                    break

            results.append(len(substring))

        return max(results) if results else 0
