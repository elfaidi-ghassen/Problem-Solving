class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            left = i
            right = i
            while True:
                if left < 0 or right >= len(s) or s[left] != s[right]:
                    break
                res += 1
                left -= 1
                right += 1
        
        for i in range(len(s)):
            left = i
            right = i + 1
            while True:
                if left < 0 or right >= len(s) or s[left] != s[right]:
                    break
                res += 1
                left -= 1
                right += 1
        return res