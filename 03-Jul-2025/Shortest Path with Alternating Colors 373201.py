# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red_edges = defaultdict(set)
        blue_edges = defaultdict(set)

        for a, b in redEdges:
            red_edges[a].add(b)

        for a, b in blueEdges:
            blue_edges[a].add(b)

        ans = [-1] * n
        queue = deque([(0, 0), (0, 1)])
        visited = set()
        edges = [red_edges, blue_edges]
        depth = 0

        while queue:
            for _ in range(len(queue)):
                node, color = queue.popleft()

                if (node,color) in visited:
                    continue
                
                if ans[node] == -1 or depth < ans[node]:
                    ans[node] = depth

                visited.add((node, color))
                children = edges[1-color].get(node, [])
                for child in children:
                    queue.append((child, 1-color))
            
            depth += 1

        return ans