from algorithm.utils.readGraph import ReadGraph
class Component:
    def __init__(self,graph):
        self.count=0
        self.visited=[False for i in range(graph.pointer())]
        self.id=[0 for i in range(graph.pointer())]
        self.graph=graph

    def component(self):
        for i in range(self.graph.pointer()):
            if not self.visited[i]:
                self.dfs(i)
                self.count+=1

    def dfs(self,v):
        self.visited[v]=True
        self.id[v]=self.count
        iter=self.graph.adjIterator(self.graph,v)
        while not iter.end():
            node=iter.next()
            if not self.visited[node]:
                self.dfs(node)
    def size(self):
        return self.count
    def isConnect(self,v,w):
        assert v>=0 and v<self.graph.pointer()
        assert w>=0 and w<self.graph.pointer()
        return self.id[v]==self.id[w]
g1=ReadGraph().readSparseGraph('testG1.txt')
c1=Component(g1)
c1.component()
print(c1.size())
g2=ReadGraph().readSparseGraph('testG2.txt')
c2=Component(g2)
c2.component()
print(c2.size())