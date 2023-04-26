class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_notes_count = {x: ransomNote.count(x) for x in ransomNote}

        for k, v in ransom_notes_count.items():
            if k not in magazine or magazine.count(k) < v:
                return False

        return True
