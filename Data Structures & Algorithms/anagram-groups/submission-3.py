class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for st in strs:
            seen[''.join(sorted(st))].append(st)

        return list(seen.values())



        