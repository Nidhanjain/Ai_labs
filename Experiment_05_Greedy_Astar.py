# Experiment 5: Greedy Best-First Search and A*
import heapq

graph = {"A": [("B", 1), ("C", 4)], "B": [("D", 2)],
         "C": [("D", 1)], "D": []}
h = {"A": 3, "B": 2, "C": 1, "D": 0}

def search(start, goal, astar=False):
    pq = [(h[start], 0, start, [start])]
    best = {start: 0}
    while pq:
        _, cost, node, path = heapq.heappop(pq)
        if node == goal:
            return path, cost
        for nxt, weight in graph[node]:
            new_cost = cost + weight
            if nxt not in best or new_cost < best[nxt]:
                best[nxt] = new_cost
                priority = new_cost + h[nxt] if astar else h[nxt]
                heapq.heappush(pq, (priority, new_cost, nxt, path + [nxt]))
    return None

print("Greedy:", search("A", "D"))
print("A*:", search("A", "D", True))
