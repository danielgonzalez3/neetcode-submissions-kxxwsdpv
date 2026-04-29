class Solution:


    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            delimiter = str(len(s)) + "#"
            res += delimiter + s
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        words = []
        while i < len(s):
            n_start = i
            n_end = i
            while s[n_end] != '#':
                n_end += 1
            count = int(s[n_start:n_end])
            words.append(s[n_end + 1 : n_end + 1 + count])
            i = n_end + 1 + count
        return words
            
