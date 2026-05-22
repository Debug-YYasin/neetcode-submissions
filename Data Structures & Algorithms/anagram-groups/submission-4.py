class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        if len(strs) == 0 or len(strs) == 1:
            return [strs]
        
        result = []
        sublist = []
        seen = set()

        for c in range(len(strs)):
            if c in seen:
                continue

            s = Counter(strs[c])
            sublist = [strs[c]]
            for i in range(c + 1, len(strs)):
                t = Counter(strs[i])
                if s == t and (i not in seen or strs[i] == ""):
                    sublist.append(strs[i])
                    seen.add(i)

            # assign shallow copy
            #  sublist[:] or sublist.copy()
            result.append(sublist[:])
            sublist.clear()
        
        return result
