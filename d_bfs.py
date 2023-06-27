graph = {
  '5': ['3','7'],
  '3': ['2', '4'],
  '7': ['8'],
  '2': [],
  '4': ['8'],
  '8': []
}


visited = set()
queue = []


def bfs(node):
    if node not in visited:
        visited.add(node)
        print(node)
        for i in graph[node]:
            queue.append(i)
        element = queue.pop(0)
        bfs(element)

bfs('5')