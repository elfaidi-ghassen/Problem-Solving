class Solution:

        
    def longestPalindrome(self, s: str) -> str:

        dp = set()
        def is_pal(i, j):
            # print(dp)
            if (i, j) in dp:
                return True
            if i == j:
                dp.add((i, j))
                return True
            if i <= j:
                if s[i] == s[j]:
                    if (j - i + 1) == 2:
                        dp.add((i, j))
                        return True
                    if (i + 1, j - 1) in dp:
                        dp.add((i, j))
                        return True
                    else:
                        return False
                    
                else:
                    return False

            else:
                dp.add((i, j))
                return True

        def solution():
            from_index, to_index = 0, 0
            mx = 0
            for i in range(len(s) - 1, -1, -1):
                for j in range(i, len(s)):
                    length = j - i + 1
                    if is_pal(i, j) and length > mx:
                        mx = length
                        from_index = i
                        to_index = j
                    # if (i, j) == (2, 4):
                        # print("ok")
                        # return s[from_index : to_index + 1]
            return s[from_index : to_index + 1]

        return solution()
