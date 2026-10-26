class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        sorted_strs = []

        for st in strs:
            sorted_strs.append(str(sorted(st)))

        for idx,val in enumerate(strs):
            seen[sorted_strs[idx]].append(val)
        
        return list(seen.values())

        