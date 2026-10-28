# Experiment 4: BFS and DFS
from collections import deque

graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"],
         "D": [], "E": [], "F": []}

def bfs(start):
    q, seen, order = deque([start]), {start}, []
    while q:
        node = q.popleft()
        order.append(node)
        for nxt in graph[node]:
            if nxt not in seen:
                seen.add(nxt)
                q.append(nxt)
    return order

def dfs(start):
    stack, seen, order = [start], set(), []
    while stack:
        node = stack.pop()
        if node not in seen:
            seen.add(node)
            order.append(node)
            stack.extend(reversed(graph[node]))
    return order

print("BFS:", bfs("A"))
print("DFS:", dfs("A"))
