import sys
from heapq import heappop, heappush
class dfs():
    def __init__(self, graph=None, visited=None):
        self.graph = dict()
        self.visited = dict()
        self.stack=list()
    
    def add_vertex(self, v, graph = None, visited = None):
        if v in graph:
            print("Vertex ", v, " already exists.")
        else:
            graph[v] = []
            visited[v]=0

  # Add an edge between vertex v1 and v2 with edge weight e
    def add_edge(self, v1, v2, e, graph = None):
        # Check if vertex v1 is a valid vertex
        if v1 not in graph:
            print("Vertex ", v1, " does not exist.")
        # Check if vertex v2 is a valid vertex
        elif v2 not in graph:
            print("Vertex ", v2, " does not exist.")
        else:
        # Since this code is not restricted to a directed or 
        # an undirected graph, an edge between v1 v2 does not
        # imply that an edge exists between v2 and v1
            temp = [v2, e]
            graph[v1].append(temp)
        # temp1=[v1,e]             #for undirected
        # self.graph[v2].append(temp1)  #for undirected
    
    def fetch_route(self, vertex, res, pred):
        while pred[vertex] != None:
            res.append(vertex)
            vertex = pred[vertex]
        res.append(vertex) #for source node

    def findShortestPaths(self, graph, source, n):
    
        # create a min-heap and push source node having distance 0
        pq = []
        heappush(pq, (0, source))
    
        # set initial distance from the source to `v` as infinity
        dist={}
        for v in graph:
            dist[v]=float('inf')
        
        # distance from the source to itself is zero
        dist[source] = 0
    
        # list to track vertices for which minimum cost is already found
        done = {}
        done[source] = True
    
        # stores predecessor of a vertex (to a print path)
        pred={}
        for v in graph:
            pred[v]=None
        
    
        # run till min-heap is empty
        while pq:
    
            node = heappop(pq)      # Remove and return the best vertex
            #u = node.vertex         # get the vertex number
            for edges in self.graph[node[1]]:
                if (dist[node[1]]+edges[1]) < dist[edges[0]]:
                    dist[edges[0]]=dist[node[1]]+edges[1]
                    pred[edges[0]]=node[1]
                    heappush(pq,(dist[edges[0]],edges[0]))

            # # do for each neighbor `v` of `u`
            # for (v, weight) in graph.adjList[u]:
            #     if not done[v] and (dist[u] + weight) < dist[v]:        # Relaxation step
            #         dist[v] = dist[u] + weight
            #         prev[v] = u
            #         heappush(pq, Node(v, dist[v]))
    
            # mark vertex `u` as done so it will not get picked up again
        
        res = []
        for key,value in self.graph.items():
            if key != source and dist[key] != sys.maxsize:
                self.fetch_route(key, res, pred)
                print(f'Path ({source} —> {key}): Minimum cost = {dist[key]}, Route = {res[::-1]}')
                res = []

        # res = []
        # for i in range(n):
        #     if i != source and dist[i] != sys.maxsize:
        #         self.fetch_route(i, res, pred)
        #         print(f'Path ({source} —> {i}): Minimum cost = {dist[i]}, Route = {route}')
        #         route.clear()
 


d = dfs()

# stores the number of vertices in the graph
vertices_no = 0
# d.add_vertex('A')
# d.add_vertex('B')
# d.add_vertex('C')
# d.add_vertex('D')
# d.add_vertex('W')

d.add_vertex('a',d.graph, d.visited)
d.add_vertex('b',d.graph, d.visited)
d.add_vertex('c',d.graph, d.visited)
d.add_vertex('d',d.graph, d.visited)
d.add_vertex('e',d.graph, d.visited)
# d.add_vertex('f',d.graph, d.visited)
# d.add_vertex('s',d.graph,d.visited)






# d.add_vertex(6,d.graph, d.visited)
# d.add_vertex(7,d.graph, d.visited)



d.add_edge('a', 'b', 10,d.graph)  
d.add_edge('a', 'e', 3,d.graph)
d.add_edge('b', 'e', 4,d.graph)
d.add_edge('b','c',2,d.graph)
d.add_edge('c', 'd', 9,d.graph)
d.add_edge('d', 'c', 7,d.graph)
d.add_edge('e', 'd', 2,d.graph)
d.add_edge('e', 'c', 8,d.graph)
d.add_edge('e', 'b', 1,d.graph)
# d.add_edge('f','e',2,d.graph)
d.findShortestPaths(d.graph,'a',5)

# Add the edges between the vertices by specifying
# the from and to vertex along with the edge weights.
# d.add_edge('A', 'B', 1)
# d.add_edge('A', 'C', 2)
# d.add_edge('D', 'A', 3)
# d.add_edge('B','D',5)
# d.add_edge(0, 1, 1, d.graph)
# d.add_edge(1, 2, 5, d.graph)
# d.add_edge(2, 3, 3, d.graph)
# d.add_edge(2, 4, 5, d.graph)
# d.add_edge(3, 0, 1, d.graph)
# d.add_edge(4, 5, 2, d.graph)
# d.add_edge(5, 6, 5, d.graph)
# d.add_edge(6, 4, 5, d.graph)
# d.add_edge(6, 7, 5, d.graph)