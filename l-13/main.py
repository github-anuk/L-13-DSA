from collections import defaultdict

class Graf:
    def __init__(self):
        self.graph=defaultdict(list)
    def adde(self,u,v):
        self.graph[u].append(v)
    def DfS_utilizer(self,v,visited):
        visited.add(v)
        print(v)
        for neighboorz in self.graph[v]:
            if neighboorz not in visited:
                self.DfS_utilizer(neighboorz,visited)
    def DFS(self,v):
        visited=set()
        self.DfS_utilizer(v,visited)

grafchild=Graf()
grafchild.adde(0,1)
grafchild.adde(0,2)
grafchild.adde(1,2)
grafchild.adde(2,0)
grafchild.adde(2,3)


grafchild.DFS(3)
