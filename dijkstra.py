import sys
from heapq import heappop, heappush

class Dijkstra():
    def __init__(self, graph=None):
        self.graph = dict()
    
    def add_vertex(self, v):
        if not self.graph.get(v):
            self.graph[v] = []

    def add_edge(self, v1, v2, e, isUndirected):
        if v1 not in self.graph:
            print("Vertex ", v1, " does not exist.")
        elif v2 not in self.graph:
            print("Vertex ", v2, " does not exist.")
        else:
            temp = [v2, e]
            self.graph[v1].append(temp)

            if isUndirected:
                temp1=[v1,e]             #for undirected
                self.graph[v2].append(temp1)  #for undirected
    
    def fetch_route(self, vertex, res, pred):
        while pred[vertex] != None:
            res.append(vertex)
            vertex = pred[vertex]
        res.append(vertex) #for source node

    def findShortestPaths(self, graph, source):
        pq = []
        heappush(pq, (0, source))

        dist={}
        for v in graph:
            dist[v]=float('inf')

        dist[source] = 0
    
        pred={}
        for v in graph:
            pred[v]=None
        while pq:
            node = heappop(pq)
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

    def dijkstra_main(self, fileName='undirectedGraph1.txt'):
        d = Dijkstra()
        fileLines = []
        with open(fileName,'r') as graph_file:
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
            d.add_vertex(vertex_src)
            d.add_vertex(vertex_dest)
            d.add_edge(vertex_src, vertex_dest, int(edge_weight), isUndirected) 

        graph_source = fileLines[-1].split(' ')[0]
        d.findShortestPaths(d.graph,graph_source)

if __name__ == "__main__":
    menu = {1: 'Undirected Graph 1', 2: 'Undirected Graph 2', 3: 'Undirected Graph 3',4: 'Undirected Graph 4', 5: 'Directed Graph 1', 6: 'Directed Graph 2', 7: 'Exit'}
    d = Dijkstra()
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
            fileName = 'undirectedGraph1.txt'
            d.dijkstra_main(fileName)

        elif select_option == 2:
            fileName = 'undirectedGraph2.txt'
            d.dijkstra_main(fileName)

        elif select_option == 3:
            fileName = 'undirectedGraph3.txt'
            d.dijkstra_main(fileName)
        
        elif select_option == 4:
            fileName = 'undirectedGraph4.txt'
            d.dijkstra_main(fileName)

        elif select_option == 5:
            fileName = 'directedGraph1.txt'
            d.dijkstra_main(fileName)

        elif select_option == 6:
            fileName = 'directedGraph2.txt'
            d.dijkstra_main(fileName)
        elif select_option == 7:
            break
        else:
            print('Please enter input from the menu options')