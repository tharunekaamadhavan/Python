graph={'5':['3','7'],
       '3':['2','4'],
       '7':['8'],
       '2':[],
       '4':['8'],
       '8':[]}
visited=[]
queue=[]
def bfs(graph,visited,node):
    visited.append(node)
    queue.append(node)
    while queue:
        a=queue.pop(0)
        print(a,end=" ")
        for neighbour in graph[a]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
bfs(graph,visited,'5')
