graph = {
  '5': ['3','7'],
  '3': ['2', '4'],
  '7': ['8'],
  '2': [],
  '4': ['8'],
  '8': []
}

visited = set()
print(graph)

def dfs(node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(neighbour)


dfs('5')