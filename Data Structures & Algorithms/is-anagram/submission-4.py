class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = Counter(t)
        if len(s) != len(t):
            return False
            
        for i in s:
            if i in seen and seen[i] > 0:
                seen[i] -= 1
            else:
                return False

        return True

        