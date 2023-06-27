# from pytictoc import TicToc
def ShortestPath(graph, n):
    mat = graph
    for k in range(n):
        for i in range(n):
            for j in range(n):
                mat[i][j] = min(mat[i][j], mat[i][k]+mat[k][j])
    printmatrix(mat,n)
def printmatrix(matrix,n):
    for i in range(n):
        for j in range(n):
            if(matrix[i][j] > 999):
                print("INF",end=" ")
            else:
                print(matrix[i][j],end=" ")
        print("\n")
n = int(input("Enter the number of nodes : "))
graph = [[0 for i in range(n)]for j in range(n)]
for i in range(n):
    for j in range(n):
        inputt = input("Enter the value at "+str(i)+" and "+str(j)+" : ")
        if(inputt == 'INF'):
            graph[i][j] += 99999
        else:
            graph[i][j] += int(inputt)
# t = TicToc()
# t.tic()
ShortestPath(graph,n)
# t.toc()