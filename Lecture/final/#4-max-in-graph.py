from collections import deque 

graph = dict() 
graph[1] = [2, 5] 
graph[2] = [1, 5, 4, 3] 
graph[5] = [6, 4, 2, 1] 
graph[4] = [6, 3, 2, 5] 
graph[3] = [2, 4, 6] 
graph[6] = [3, 4, 5] 


def max_graph(graph, root):
    graph_queue = deque([root]) 
    node = root 
    maxVal = 0
    while len(graph_queue) > 0:
        node = graph_queue.popleft() 
        adj_nodes = graph[node] 
        print("max is", max(adj_nodes), node)
        maxVal = max(adj_nodes)

print(graph)

print(max_graph(graph, 3)) #6
print(max_graph(graph, 6)) #5