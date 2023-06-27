# # from pytictoc import TicToc
# class Graph:
#     def _init_(self, vertices):
#         self.V = vertices
#         self.graph = []
#     def addEdge(self,u,v,w):
#         self.graph.append([u,v,w])
#     def find(self, parent, i):
#         if parent[i] != i:
#             self.find(parent, parent[i])
#         else:
#             return i
#     def union(self, parent, rank, x, y):
#         xt = self.find(parent, x)
#         yt = self.find(parent, y)
#         if(rank[xt] < rank[yt]):
#             parent[xt] = yt
#         elif(rank[xt] > rank[yt]):
#             parent[yt] = xt
#         else:
#             parent[xt] = yt
#             rank[yt] += 1
#     def Kurshkal(self):
#         result = []
#         i = 0
#         e = 0
#         self.graph = sorted(self.graph, key = lambda itm:itm[2])
#         parent = []
#         rank = []
#         for node in range(self.V):
#             parent.append(node)
#             rank.append(0)
#         while(e<self.V-1):
#             u, v, w = self.graph[i]
#             i += 1
#             x = self.find(parent, u)
#             y = self.find(parent, v)
#             if(x!=y):
#                 e+=1
#                 result.append([u,v,w])
#                 self.union(parent, rank, x, y)
#         minCost = 0
#         for u,v,w in result:
#             minCost += w
#         return result, minCost
# # t = TicToc()
# n = int(input("Enter the number of vertices : "))
# ed = int(input("Enter the number of edges : "))
# graph = Graph(n)
# for i in range(ed):
#     input1 = int(input("Enter the vertex 1 for edge %d : "%(i)))
#     input2 = int(input("Enter the vertex 2 for edge %d : " % (i)))
#     weight = int(input("Enter the weight for edge %d : " % (i)))
#     graph.addEdge(input1, input2, weight)
# # t.tic()
# result, minCost = graph.Kurshkal()
# # t.toc()
# print("  Edge  : weight")
# for u, v, w in result:
#     print("  %d - %d :  %d"%(u,v,w))
# print("The Minimum Spanning Tree : ",minCost)
def kruskalAlgo(self):
    i, e = 0, 0
    ds = dst.DisjointSet(self.nodes)
    self.graph = sorted(self.graph, key=lambda item: item[2])
    while e < self.V - 1:
        s, d, w = self.graph[i]
        i += 1
        x = ds.find(s)
        y = ds.find(d)
        if x != y:
            e += 1
            self.MST.append([s,d,w])
            ds.union(x,y)
    self.printSolution(s,d,w)

g = Graph(5)
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")
g.addEdge("A", "B", 5)
g.addEdge("A", "C", 13)
g.addEdge("A", "E", 15)
g.addEdge("B", "A", 5)
g.addEdge("B", "C", 10)
g.addEdge("B", "D", 8)
g.addEdge("C", "A", 13)
g.addEdge("C", "B", 10)
g.addEdge("C", "E", 20)
g.addEdge("C", "D", 6)
g.addEdge("D", "B", 8)
g.addEdge("D", "C", 6)
g.addEdge("E", "A", 15)
g.addEdge("E", "C", 20)

g.kruskalAlgo()