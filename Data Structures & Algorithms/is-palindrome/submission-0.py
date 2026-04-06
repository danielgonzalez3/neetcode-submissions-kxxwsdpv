class Solution:
    def isPalindrome(self, s: str) -> bool:
        l_idx = 0
        r_idx = len(s) - 1
        while (l_idx <= r_idx):
            if (not s[l_idx].isalnum()):
                l_idx +=1
                continue
            if (not s[r_idx].isalnum()):
                r_idx -=1
                continue
            if s[l_idx].lower() != s[r_idx].lower():
                return False
            l_idx +=1
            r_idx -=1
        return True
            