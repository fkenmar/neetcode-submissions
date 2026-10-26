class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)

        for st in strs:
            seen[str(sorted(st))].append(st)
        
        return list(seen.values())
        