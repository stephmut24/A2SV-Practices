# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return 
        if rootX < rootY:
            self.parent[rootY] = rootX
        else:
            self.parent[rootX] = rootY

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges)+1)

        for i in range(len(edges)):
            if uf.find(edges[i][0]) != uf.find(edges[i][1]):
                uf.union(edges[i][0], edges[i][1])
            else:
                return edges[i]