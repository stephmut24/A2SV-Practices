# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        reverse_graph = defaultdict(list)
        out_degree = [0] * n
        
        # Build reverse graph and out-degree count
        for u in range(n):
            for v in graph[u]:
                reverse_graph[v].append(u)
            out_degree[u] = len(graph[u])
        
        # Start with terminal nodes (out_degree == 0)
        queue = deque([i for i in range(n) if out_degree[i] == 0])
        safe = [False] * n
        
        while queue:
            node = queue.popleft()
            safe[node] = True
            for parent in reverse_graph[node]:
                out_degree[parent] -= 1
                if out_degree[parent] == 0:
                    queue.append(parent)
        
      
        return [i for i in range(n) if safe[i]]