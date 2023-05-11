class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        occurrences = {x: nums.count(x) for x in nums}

        return [x for x in occurrences.keys() if occurrences[x] == 1][0]
