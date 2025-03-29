class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for source, dest, cost in times:
            edges[source].append((dest, cost))

        queue = [(0, k)]
        visit = set()
        t = 0
        while queue:
            cost, node = heappop(queue)
            if node in visit:
                continue
            
            visit.add(node)
            t = max(t, cost)

            for nei, cost_nei in edges[node]:
                if nei not in visit:
                    heappush(queue, (cost+ cost_nei, nei))
        
        return t if len(visit) == n else -1