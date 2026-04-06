class Solution:
    def isValid(self, s: str) -> bool:
        mappings = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        stack = []
        
        for ch in s:
            # opening bracket → push
            if ch in "({[":
                stack.append(ch)
            else:
                # closing bracket but stack empty
                if not stack:
                    return False
                # must match the last opening
                if stack.pop() != mappings[ch]:
                    return False

        return len(stack) == 0
