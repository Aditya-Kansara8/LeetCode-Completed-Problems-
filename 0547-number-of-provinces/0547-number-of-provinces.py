class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        count = 0

        def dfs(i):
            visited.add(i)
            for j, connection in enumerate(isConnected[i]):
                if connection == 1 and j not in visited:
                    dfs(j)

        for i in range(len(isConnected)):
            if i not in visited:
                count += 1
                dfs(i)

        return count