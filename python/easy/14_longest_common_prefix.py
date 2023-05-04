class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_word = min(strs)
        prefix = ''

        for i in range(len(shortest_word)):
            if all([x[i] == shortest_word[i] for x in strs]):
                prefix += shortest_word[i]
            else:
                break

        return prefix