class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = defaultdict(int)
        for ch in s:
            seen[ch] += 1
        for ch in t:
            seen[ch] -= 1

        return all(val == 0 for val in seen.values())
        
        