class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = self.clean_str(s)
        s_length = len(s)
        for i in range(s_length // 2):
            print(s[i], s[s_length - i - 1])
            if (s[i] != s[s_length - i - 1]):
                return False
        return True

    def clean_str(self, string):
        valid = "abcdefghijklmnopqrstuvwxyz0123456789"
        clean = ""
        for s in string:
            if s.lower() in valid:
                clean += s.lower()
        return clean