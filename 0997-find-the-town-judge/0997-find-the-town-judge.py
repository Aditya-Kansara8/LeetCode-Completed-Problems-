class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_count = [0] * (n + 1) 
        trusts_someone = [False] * (n + 1) 
        
        for a, b in trust:
            trusts_someone[a] = True
            trust_count[b] += 1
        
        for i in range(1, n + 1):
            if not trusts_someone[i] and trust_count[i] == n - 1:
                return i
        
        return -1     