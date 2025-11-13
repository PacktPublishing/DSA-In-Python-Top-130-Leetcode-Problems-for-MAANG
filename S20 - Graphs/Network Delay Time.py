class Solution:
    def computeDistance(self, graph, k):
        dist = [math.inf] * len(graph)
        pq = [(0, k)]
        dist[k] = 0

        while pq:
            currentDistance, top = heapq.heappop(pq)
            if dist[top] < currentDistance:
                continue

            for v, w in graph[top]:
                if dist[v] > currentDistance + w:
                    dist[v] = currentDistance + w
                    heapq.heappush(pq, (dist[v], v))

        return dist
        
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = [[] for _ in range(N)]
        for edge in times:
            u, v, w = edge[0] - 1, edge[1] - 1, edge[2]
            graph[u].append((v, w))

        distance = self.computeDistance(graph, K - 1)
        ma = max(distance)
        if ma == math.inf:
            return -1
        else:
            return ma
    
