class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in connections:
            graph[a].append((b, 1))  # needs flip
            graph[b].append((a, 0))  # already correct
        
        visited = {0}
        queue = deque([0])
        count = 0
        
        while queue:
            node = queue.popleft()
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    count += weight
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return count