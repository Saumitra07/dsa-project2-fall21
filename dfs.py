# Add a vertex to the dictionary
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
  
  def reverse_graph(self, original_graph, reverse_graph, rev_graph_visited):
    for key in original_graph.keys():
      self.add_vertex(key, reverse_graph, rev_graph_visited)
    #debug
    # a = reverse_graph
    # b = self.graph
    # c = rev_graph_visited
    # d = self.visited
    for src, value in original_graph.items():
      for dest in value:
        self.add_edge(dest[0], src, dest[1], reverse_graph)
      
    # a = reverse_graph
    # b = self.graph
    # c = rev_graph_visited
    # d = self.visited


  # Print the graph
  def print_graph(self):
    for vertex in self.graph:
      for edges in self.graph[vertex]:
        print(vertex, " -> ", edges[0], " edge weight: ", edges[1])


  def dfs_visit(self, v,visited):
    visited[v]=1
    print(v)
    for edges in self.graph[v]:
      if self.visited[edges[0]]!=1:
        self.dfs_visit(edges[0],self.visited)
       
    self.stack.append(v)

  def scc_dfs(self,v, reverse_graph, reverse_visited, res):
    reverse_visited[v] = 1
    res.append(v)
    #print(v, end='')
    for edges in reverse_graph[v]:
      if reverse_visited[edges[0]]!=1:
        self.scc_dfs(edges[0], reverse_graph ,reverse_visited, res)

  def dfs_main(self):
    for key, value in self.graph.items():
        if self.visited[key] != 1:
          self.dfs_visit(key,self.visited)
  
  def strongly_connected_components_driver(self):
    reverse_graph = dict()
    reverse_graph_visited = dict()
    res = []
    final = []
    #DFS on orig graph and creation of stack according to finish times
    self.dfs_main()

    self.reverse_graph(self.graph, reverse_graph, reverse_graph_visited)

    while self.stack:
      vertex = self.stack.pop()
      if reverse_graph_visited[vertex] != 1:
        self.scc_dfs(vertex, reverse_graph, reverse_graph_visited, res)
        final.append(res)
        res = []
    return final
      
# driver code
d = dfs()

# stores the number of vertices in the graph
vertices_no = 0
# d.add_vertex('A')
# d.add_vertex('B')
# d.add_vertex('C')
# d.add_vertex('D')
# d.add_vertex('W')

d.add_vertex(0,d.graph, d.visited)
d.add_vertex(1,d.graph, d.visited)
d.add_vertex(2,d.graph, d.visited)
d.add_vertex(3,d.graph, d.visited)
d.add_vertex(4,d.graph, d.visited)
d.add_vertex(5,d.graph, d.visited)
d.add_vertex(6,d.graph, d.visited)
d.add_vertex(7,d.graph, d.visited)

# Add the edges between the vertices by specifying
# the from and to vertex along with the edge weights.
# d.add_edge('A', 'B', 1)
# d.add_edge('A', 'C', 2)
# d.add_edge('D', 'A', 3)
# d.add_edge('B','D',5)
d.add_edge(0, 1, 1, d.graph)
d.add_edge(1, 2, 5, d.graph)
d.add_edge(2, 3, 3, d.graph)
d.add_edge(2, 4, 5, d.graph)
d.add_edge(3, 0, 1, d.graph)
d.add_edge(4, 5, 2, d.graph)
d.add_edge(5, 6, 5, d.graph)
d.add_edge(6, 4, 5, d.graph)
d.add_edge(6, 7, 5, d.graph)



d.print_graph()
# Reminder: the second element of each list inside the dictionary
# denotes the edge weight.
print ("Internal representation: ", d.graph)
print("visited:     ",d.visited)
#d.dfs_main()
#print(d.visited)
#print("stack is",d.stack)

#d.reverse_graph(d.graph)
print(d.strongly_connected_components_driver())