from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grams = dict()
        for s in strs:
            key = ''.join(sorted(s))
            if key not in grams:
                grams[key] = []
            grams[key].append(s)
        return list(grams.values())