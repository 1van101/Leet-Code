class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums_sorted = sorted(nums1)
        mid = len(nums_sorted) // 2

        if len(nums_sorted) % 2 == 1:
            res = nums_sorted[mid]
        else:
            res = (nums_sorted[mid] + nums_sorted[mid - 1]) / 2

        return res