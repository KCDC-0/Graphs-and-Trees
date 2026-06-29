######## Graph ########

graph = {
    "1": ["2", "9"],
    "2": ["1"],
    "3": ["4", "5", "6", "9"],
    "4": ["3"],
    "5": ["3", "8"],
    "6": ["3", "7"],
    "7": ["6", "8", "9"],
    "8": ["5", "7"],
    "9": ["1", "3", "7"],
    "10": [] 
}

graph2 = [[0, 16, 13, 0, 0, 0],
		[0, 0, 10, 12, 0, 0],
		[0, 4, 0, 0, 14, 0],
		[0, 0, 9, 0, 0, 20],
		[0, 0, 0, 7, 0, 4],
		[0, 0, 0, 0, 0, 0]]

######## Graph Traversals ########

def bfs(graph, start_node, target_node):
    queue = [start_node]
    layer = [0]
    discovered = [start_node]
    neighbours = []
    found = False
    counter = 0
    while len(queue) != 0 and found == False:
        current_node = queue[0]
        queue = queue[1:]
        counter = layer[0]
        layer = layer[1:]
        neighbours = graph[current_node]
        for node in neighbours:
            if node not in discovered:
                if node == target_node:
                    counter += 1
                    found = True
                else:
                    queue.append(node)
                    discovered.append(node)
                    layer.append(counter + 1)
    return found, int(found) * counter

def dfs(graph, start_node, target_node):
    stack = [start_node]
    discovered = [start_node]
    neighbours = []
    found = False
    while len(stack) != 0 and found == False:
        current_node = stack.pop()
        neighbours = graph[current_node]
        for node in neighbours:
            if node not in discovered:
                if node == target_node:
                    found = True
                else:
                    stack.append(node)
                    discovered.append(node)    
    return found, stack, discovered

######## Kruskal's Algorithm ########

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for i in range(vertices)] for e in range(vertices)]

    def printSolution(self, dist):
        print(f"{'Vertex':<10} | {'Distance from Source':<20}")
        print("-" * 35)
        for node in range(self.V):
            print(f"{node:<10} | {dist[node]:<20}")

    def printMST(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[parent[i]][i])


    ## Old

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1

    def KruskalMST(self):
        result = []
        i = 0
        e = 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
        minimumCost = 0
        print("Edges in the constructed MST")
        for u, v, weight in result:
            minimumCost += weight
            print("%d -- %d == %d" % (u, v, weight))
        print("Minimum Spanning Tree", minimumCost)


    ## New

    def minDistance(self, dist, sptSet):
        min = 1e7

        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index

    
    def dijkstra(self, src):
        dist = [1e7] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for c in range(self.V):
            u = self.minDistance(dist, sptSet)

            sptSet[u] = True

            for v in range(self.V):
                if (self.graph[u][v] > 0 and 
                   sptSet[v] == False and 
                   dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(dist)

    def primMST(self):
        key = [1e7] * self.V
        parent = [None]
        
        key[0] = 0
        mstSet = [False] * self.V
        parent[0] = -1

        for c in range(self.V):
            u = self.minDistance(key, mstSet)
            mstSet[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and mstSet[v] == False \
                and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.printMST(parent)


######## Ford Fulkerson (max flow) ########

def bfs_parent(graph, s, t, parent):
        visited = [False]*(len(graph))
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
                u = queue.pop(0)
                for ind, val in enumerate(graph[u]):
                        if visited[ind] == False and val > 0:
                                queue.append(ind)
                                visited[ind] = True
                                parent[ind] = u
                                if ind == t:
                                        return True
        return False

def FordFulkerson(graph, source, sink):
        parent = []
        for i in range(len(graph)):
            parent.append(-1)
        max_flow = 0
        while bfs_parent(graph, source, sink, parent) :
                path_flow = float("Inf")
                s = sink
                while(s != source):
                        path_flow = min(path_flow, graph[parent[s]][s])
                        s = parent[s]
                max_flow += path_flow
                v = sink
                while(v != source):
                        u = parent[v]
                        graph[u][v] -= path_flow
                        graph[v][u] += path_flow
                        v = parent[v]
        return max_flow














