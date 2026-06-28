class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        count = [0] * (n+1)

        for a,b in edges:
            count[a] += 1
            count[b] += 1
        
        return count.index(max(count))

