class strongly_connected_component():
  def __init__(self, graph=None, visited=None):
    self.graph = dict()
    self.visited = dict()
    self.stack=list()
  
  def add_vertex(self, v, graph, visited):
        if not graph.get(v):
            graph[v] = []
            visited[v]=0

  def add_edge(self, v1, v2, e, graph = None):
    if v1 not in graph:
      print("Vertex ", v1, " does not exist.")
    elif v2 not in graph:
      print("Vertex ", v2, " does not exist.")
    else:
      temp = [v2, e]
      graph[v1].append(temp)
  
  def reverse_graph(self, original_graph, reverse_graph, rev_graph_visited):
    for key in original_graph.keys():
      self.add_vertex(key, reverse_graph, rev_graph_visited)
      
    for src, value in original_graph.items():
      for dest in value:
        self.add_edge(dest[0], src, dest[1], reverse_graph)
      
  def dfs_visit(self, v,visited):
    visited[v]=1
    for edges in self.graph[v]:
      if self.visited[edges[0]]!=1:
        self.dfs_visit(edges[0],self.visited)
       
    self.stack.append(v)

  def scc_dfs(self,v, reverse_graph, reverse_visited, res):
    reverse_visited[v] = 1
    res.append(v)
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
    self.dfs_main()

    self.reverse_graph(self.graph, reverse_graph, reverse_graph_visited)

    while self.stack:
      vertex = self.stack.pop()
      if reverse_graph_visited[vertex] != 1:
        self.scc_dfs(vertex, reverse_graph, reverse_graph_visited, res)
        final.append(res)
        res = []
    return final

  def scc_main(self, fileName='directedGraph1.txt'):
        sc = strongly_connected_component()
        fileLines = []
        with open(fileName,'r') as graph_file:
            fileLines = graph_file.read().splitlines() 

        graph_info = fileLines[0].split(' ')
        number_of_vertices = graph_info[0]
        number_of_edges = graph_info[1]

        for i in range(1, len(fileLines)-1):
            edge_info = fileLines[i].split(' ')
            vertex_src = edge_info[0]
            vertex_dest = edge_info[1]
            edge_weight = edge_info[2]
            sc.add_vertex(vertex_src, sc.graph, sc.visited)
            sc.add_vertex(vertex_dest, sc.graph, sc.visited)
            sc.add_edge(vertex_src, vertex_dest, int(edge_weight),sc.graph) 

        print(sc.strongly_connected_components_driver())
      
if __name__ == "__main__":
    menu = { 1: 'Directed Graph 1', 2: 'Directed Graph 2',3: 'Directed Graph 3',4: 'Directed Graph 4', 5: 'Exit'}
    d = strongly_connected_component()
    fileName = ''
    while True:
        print('--------------------------------------------------')
        for key, value in menu.items():
            print(key,'-',value)
        
        select_option = ''
        try:
            select_option = int(input('Please select the graph to be used to run the Dijkstra algorithm: '))
        except:
            print('Please input a number')


        if select_option == 1:
            fileName = 'scc_1.txt'
            d.scc_main(fileName)

        elif select_option == 2:
            fileName = 'directedGraph1.txt'
            d.scc_main(fileName)

        elif select_option == 3:
            fileName = 'directedGraph2.txt'
            d.scc_main(fileName)

        elif select_option == 4:
            fileName = 'directedGraph2.txt'
            d.scc_main(fileName)
        elif select_option == 5:
            break
        else:
            print('Please enter input from the menu options')