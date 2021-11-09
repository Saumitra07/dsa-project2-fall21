# Add a vertex to the dictionary
def add_vertex(v):
  global graph
  global vertices_no
  if v in graph:
    print("Vertex ", v, " already exists.")
  else:
    vertices_no = vertices_no + 1
    graph[v] = []
    visited[v]=0

# Add an edge between vertex v1 and v2 with edge weight e
def add_edge(v1, v2, e):
  global graph
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
    # temp1=[v1,e]             for undirected
    # graph[v2].append(temp1)  for undirected

# Print the graph
def print_graph():
  global graph
  for vertex in graph:
    for edges in graph[vertex]:
      print(vertex, " -> ", edges[0], " edge weight: ", edges[1])


def dfs_visit(v,visited):
  visited[v]=1
  print(v)
  for edges in graph[v]:
    if visited[edges[0]]!=1:
      dfs_visit(edges[0],visited)

def dfs(v,visited):
  
  dfs_visit(v,visited)

# driver code
graph = {}
visited={}
# stores the number of vertices in the graph
vertices_no = 0
add_vertex('A')
add_vertex('B')
add_vertex('C')
add_vertex('D')
# Add the edges between the vertices by specifying
# the from and to vertex along with the edge weights.
add_edge('A', 'B', 1)
add_edge('A', 'C', 2)
add_edge('D', 'A', 3)
add_edge('B','D',5)
# add_edge(3, 4, 4)
# add_edge(4, 1, 5)
print_graph()
# Reminder: the second element of each list inside the dictionary
# denotes the edge weight.
print ("Internal representation: ", graph)
print("visited:     ",visited)
dfs('A',visited)