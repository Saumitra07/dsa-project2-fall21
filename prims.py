import sys
from heapq import heappop, heappush

class Prims():
    def __init__(self, graph=None):
        self.graph = dict()
    
    def add_vertex(self, v):
        if not self.graph.get(v):
            self.graph[v] = []

    def add_edge(self, v1, v2, e,isUndirected):
        if v1 not in self.graph:
            print("Vertex ", v1, " does not exist.")
        elif v2 not in self.graph:
            print("Vertex ", v2, " does not exist.")
        else:
            temp = [v2, e]
            self.graph[v1].append(temp)
            temp1=[v1,e]             #for undirected
            self.graph[v2].append(temp1)  #for undirected
    
    def prims_min_spanning_tree(self, graph, source):
        pq = []
        heappush(pq, (0, source))

        keys = {}
        for v in graph:
            keys[v] = float('inf')
        
        keys[source] = 0

        pred={}
        for v in graph:
            pred[v]=None

        visited = {}
        for v in graph:
            visited[v] = False

        while pq:
            node = heappop(pq)
            visited[node[1]] = True
            for edges in graph[node[1]]:
                if visited[edges[0]] == False and keys[edges[0]] > edges[1]:
                    keys[edges[0]] = edges[1]
                    heappush(pq, (edges[1], edges[0]))
                    pred[edges[0]] = node[1]

        sum=0
        for key in keys:
            sum+=keys[key]
        
        for key, val in pred.items():
            if key != source:
                print('Edge',":",'(',val, ",", key,')',end=' ')
                print('Weight:',keys[key])
        print('Total Cost of minimum spanning tree is:', sum)

    def prims_main(self, fileName='undirectedGraph1.txt'):
        p = Prims()
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
            p.add_vertex(vertex_src)
            p.add_vertex(vertex_dest)
            p.add_edge(vertex_src, vertex_dest, int(edge_weight), isUndirected) 

        graph_source = fileLines[-1].split(' ')[0]
        p.prims_min_spanning_tree(p.graph,graph_source)

if __name__ == "__main__":
    menu = {1: 'Undirected Graph 1', 2: 'Undirected Graph 2', 3: 'Undirected Graph 3',4: 'Undirected Graph 4', 5: 'Exit'}
    prims = Prims()
    fileName = ''
    while True:
        print('--------------------------------------------------')
        for key, value in menu.items():
            print(key,'-',value)
        
        select_option = ''
        try:
            select_option = int(input('Please select the graph to be used to run  the prims algorithm: '))
        except:
            print('Please input a number')
        
        if select_option == 1:
            fileName = 'undirectedGraph1.txt'
            prims.prims_main(fileName)

        elif select_option == 2:
            fileName = 'undirectedGraph2.txt'
            prims.prims_main(fileName)

        elif select_option == 3:
            fileName = 'undirectedGraph3.txt'
            prims.prims_main(fileName)
        
        elif select_option == 4:
            fileName = 'undirectedGraph4.txt'
            prims.prims_main(fileName)

        elif select_option == 5:
            break
        else:
            print('Please enter input from the menu options')