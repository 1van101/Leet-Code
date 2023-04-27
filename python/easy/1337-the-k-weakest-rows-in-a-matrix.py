class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldiers = {x: mat[x].count(1) for x in range(len(mat))}
        soldiers_sorted = sorted(soldiers.items(), key=lambda x: x[1])

        return [x[0] for x in soldiers_sorted[:k]]