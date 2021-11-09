# Add a vertex to the dictionary
class dfs():
  def __init__(self, graph=None, visited=None):
    self.graph = dict()
    self.visited = dict()
    self.stack=list()
  def add_vertex(self, v):
    if v in self.graph:
      print("Vertex ", v, " already exists.")
    else:
      self.graph[v] = []
      self.visited[v]=0

  # Add an edge between vertex v1 and v2 with edge weight e
  def add_edge(self, v1, v2, e):
    # Check if vertex v1 is a valid vertex
    if v1 not in self.graph:
      print("Vertex ", v1, " does not exist.")
    # Check if vertex v2 is a valid vertex
    elif v2 not in self.graph:
      print("Vertex ", v2, " does not exist.")
    else:
      # Since this code is not restricted to a directed or 
      # an undirected graph, an edge between v1 v2 does not
      # imply that an edge exists between v2 and v1
      temp = [v2, e]
      self.graph[v1].append(temp)
      # temp1=[v1,e]             #for undirected
      # self.graph[v2].append(temp1)  #for undirected

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


  def dfs_main(self):
    for key, value in self.graph.items():
        if self.visited[key] != 1:
          self.dfs_visit(key,self.visited)

# driver code
d = dfs()

# stores the number of vertices in the graph
vertices_no = 0
# d.add_vertex('A')
# d.add_vertex('B')
# d.add_vertex('C')
# d.add_vertex('D')
# d.add_vertex('W')

d.add_vertex(0)
d.add_vertex(1)
d.add_vertex(2)
d.add_vertex(3)
d.add_vertex(4)
d.add_vertex(5)
d.add_vertex(6)
d.add_vertex(7)

# Add the edges between the vertices by specifying
# the from and to vertex along with the edge weights.
# d.add_edge('A', 'B', 1)
# d.add_edge('A', 'C', 2)
# d.add_edge('D', 'A', 3)
# d.add_edge('B','D',5)
d.add_edge(0, 1, 1)
d.add_edge(1, 2, 5)
d.add_edge(2, 3, 3)
d.add_edge(2, 4, 5)
d.add_edge(3, 0, 1)
d.add_edge(4, 5, 2)
d.add_edge(5, 6, 5)
d.add_edge(6, 4, 5)
d.add_edge(6, 7, 5)



d.print_graph()
# Reminder: the second element of each list inside the dictionary
# denotes the edge weight.
print ("Internal representation: ", d.graph)
print("visited:     ",d.visited)
d.dfs_main()
print(d.visited)
print("stack is",d.stack)