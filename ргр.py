from collections import defaultdict
 
class Graph:
 
    def __init__(self, graph):
        self.graph = graph  
        self. ROW = len(graph)
        # self.COL = len(gr[0])
 
 
    def BFS(self, s, t, parent):
 
        visited = [False]*(self.ROW)
 
        queue = []
 
        queue.append(s)
        visited[s] = True
 
        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
                    if ind == t:
                        return True
        return False
             
     
    def FordFulkerson(self, source, sink):
        parent = [-1]*(self.ROW)
        max_flow = 0 
        while self.BFS(source, sink, parent) :
            path_flow = float("Inf")
            s = sink
            while(s !=  source):
                path_flow = min (path_flow, self.graph[parent[s]][s])
                s = parent[s]
            max_flow +=  path_flow
            v = sink
            while(v !=  source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
        return max_flow

count = int(input("Input number of vertices:"))
graph = []
for i in range(0,count):
    list = []
    for j in range(0,count):
        element = input(f"Input a[{i+1}][{j+1}] element:")
        if element == 'inf':
            element = float('inf')
        else:
            element = int(element)
        list.insert(len(list),element)
    graph.insert(len(graph),list)
print(graph)
'''
graph = [[0, float('inf'), float('inf'), 0, 0, 0],
[0, 0, 0, 2, 1, 0],
[0, 0, 0, 3, 0, 4],
[0, 0, 0, 0, 0, 5],
[0, 0, 0, 0, 0, 6],
[0, 0, 0, 0, 0, 0]]
print(graph)
'''
g = Graph(graph)
source = int(input("Input source of graph "))
sink = int(input("Input sink of graph "))
result1 = g.FordFulkerson(source, sink)
print ("The maximum possible flow is %d " % result1)
c = int(input("Как много новых колодцев/ домов вы хотите добавить? Введите число "))
count = 6
newlist = []
for i in range(0,c):
    n = []
    for j in range(0,c+count):
        element = input(f"Input a[{count+i+1}][{j+1}] element: ")
        if element == 'inf':
            element = float('inf')
        else:
            element = int(element)
        n.insert(len(n),element)
    newlist.insert(len(newlist),n)
print(f"newlist: {newlist}")

for i in range(0,count):
    for j in range(0,c):
        element = input(f"Input a[{i+1}][{count+j+1}] element: ")
        if element == 'inf':
            element = float('inf')
        else:
            element = int(element)
        graph[i].insert(len(graph[i]),element)
    print(f"graph[i]: {graph[i]}")

for i in range(0,len(newlist)):
    graph.insert(len(graph),newlist[i])
print(graph)
g2 = Graph(graph)
source2 = int(input("input source in new graph "))
sink2 = int(input("input sink in new graph "))
result2 = g2.FordFulkerson(source2, sink2)
print(f"result2: {result2}")
if result2>result1:
    print("То, что вы хотели добавить, увы, добавить нельзя ")
else:
    print("Добавить можно. Всё ок ")
    
 
