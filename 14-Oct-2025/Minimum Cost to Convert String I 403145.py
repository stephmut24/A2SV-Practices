# Problem: Minimum Cost to Convert String I - https://leetcode.com/problems/minimum-cost-to-convert-string-i/description/?envType=problem-list-v2&envId=shortest-path

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        from heapq import heappop, heappush
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        g1 = [[float('inf') for _ in range(26)] for _ in range(26)]
        def vg(char):
            return ord(char) - ord('a')
        def gv(idx):
            return chr(ord('a') + idx)

        for i in range(len(original)):
            u,v,w = vg(original[i]), vg(changed[i]), cost[i]
            w = min(g1[u][v], w)
            g1[u][v] = w

        g = defaultdict(list)   
        for i in range(26):
            for j in range(26):
                if g1[i][j] != float('inf'):
                    g[gv(i)].append((gv(j), g1[i][j]))
        def dijkstra(src, tgt):
            ans = float('inf')
            hp = [(0, src)]
            seen = set()

            while hp:
                c, u = heappop(hp)
                if u in seen: continue
                seen.add(u)

                for v, w in g[u]:
                    d = c + w
                    if v == tgt: ans = min(ans, d)
                    if v not in seen:
                        heappush(hp, (d, v))
            return ans
        mp = [[float('inf') for j in range(26)] for _ in range(26)]
        for i in range(26):
            for j in range(26):
                mp[i][j] = dijkstra(chr(i + ord('a')),chr(j + ord('a')))

        ans = 0
        for i in range(len(source)):
            s,t= source[i],target[i]
            if s == t: continue
            a = mp[ord(s) - ord('a')][ord(t) - ord('a')]
            if(a == float('inf')): return -1
            ans += a
        return ans
        