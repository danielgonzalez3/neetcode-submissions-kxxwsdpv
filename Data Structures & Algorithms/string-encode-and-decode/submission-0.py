class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for s in strs:
            encoded += f'{len(s)}#{s}'
        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded = []
        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])
            i = j + 1
            decoded.append(s[i:i + length])
            i += length
        return decoded
