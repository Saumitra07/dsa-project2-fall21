import sys
from heapq import heappop, heappush

class dfs():
    def __init__(self, graph=None):
        self.graph = dict()
    
    def add_vertex(self, v, graph = None, visited = None):
        if not graph.get(v):
            graph[v] = []
            visited[v]=0

  # Add an edge between vertex v1 and v2 with edge weight e
    def add_edge(self, v1, v2, e, isUndirected,graph = None):
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

            if isUndirected:
                temp1=[v1,e]             #for undirected
                self.graph[v2].append(temp1)  #for undirected
    
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
        res = []
        for key,value in self.graph.items():
            if key != source and dist[key] != sys.maxsize:
                self.fetch_route(key, res, pred)
                print(f'Path ({source} —> {key}): Minimum cost = {dist[key]}, Route = {res[::-1]}')
                res = []

d = dfs()

fileLines = []
with open('undirectedGraph_1.txt','r') as graph_file:
    fileLines = graph_file.read().splitlines() 

graph_info = fileLines[0].split(' ')
number_of_vertices = graph_info[0]
number_of_edges = graph_info[1]
isUndirected = False
if str(graph_info[2]).lower() == 'u':
    isUndirected = True

for i in range(1, len(fileLines)-1):
    edge_info = fileLines[i].split(' ')
    vertex_src = edge_info[0]
    vertex_dest = edge_info[1]
    edge_weight = edge_info[2]
    d.add_vertex(vertex_src,d.graph, d.visited)
    d.add_vertex(vertex_dest,d.graph, d.visited)
    d.add_edge(vertex_src, vertex_dest, int(edge_weight), isUndirected,d.graph) 

graph_source = fileLines[-1].split(' ')[0]
d.findShortestPaths(d.graph,graph_source,9)

# for line in fileLines:
#     l = line.split(' ')
#     last = l[2]
# stores the number of vertices in the graph
vertices_no = 0
# d.add_vertex('A')
# d.add_vertex('B')
# d.add_vertex('C')
# d.add_vertex('D')
# d.add_vertex('W')

# d.add_vertex('a',d.graph, d.visited)
# d.add_vertex('b',d.graph, d.visited)
# d.add_vertex('c',d.graph, d.visited)
# d.add_vertex('d',d.graph, d.visited)
# d.add_vertex('e',d.graph, d.visited)
# d.add_vertex('f',d.graph,d.visited)
# d.add_vertex('g',d.graph,d.visited)
# d.add_vertex('h',d.graph,d.visited)
# d.add_vertex('i',d.graph,d.visited)


# d.add_edge('a', 'c', 5,d.graph)  
# d.add_edge('a', 'e', 4,d.graph)
# d.add_edge('a', 'f', 2,d.graph)
# d.add_edge('b','e',6,d.graph)
# d.add_edge('b', 'f', 6,d.graph)
# d.add_edge('c', 'd', 3,d.graph)
# d.add_edge('d', 'h', 7,d.graph)
# d.add_edge('h', 'g', 7,d.graph)
# d.add_edge('g', 'e', 4,d.graph)
# d.add_edge('g', 'i', 5,d.graph)
# d.add_edge('i', 'b', 2,d.graph)
# d.add_edge('e', 'd', 6,d.graph)
# d.add_edge('d', 'a', 2,d.graph)

# d.add_edge('f','e',2,d.graph)
# d.findShortestPaths(d.graph,'d',9)

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