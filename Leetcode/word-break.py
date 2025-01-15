class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        dp = set()
        def solution(k):
            if k >= len(s):
                return True
            sol = False
            if k in dp:
                return False


            w = ""
            for i in range(k, len(s)):
                w += s[i]
                if w in wordDict:
                    next_sol = solution(i + 1)
                    sol = sol or next_sol
                    
            if not sol:
                dp.add(k)   
            return sol
        return solution(0)