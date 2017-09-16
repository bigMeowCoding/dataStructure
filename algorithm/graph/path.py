from algorithm.utils.readGraph import ReadGraph
class Path:
    def __init__(self,s,graph):
        self.visited=[False for i in range(graph.pointer())]
        assert s>=0 and s<graph.pointer()
        self.s=s
        self.graph=graph
        self.froms= [-1 for i in range(graph.pointer())]

    def path(self):
        self.dfs(self.s)

    def dfs(self,v):
        self.visited[v]=True
        iter=self.graph.adjIterator(self.graph,v)
        while not iter.end():
            node=iter.next()
            if not self.visited[node]:
                self.froms[node]=v
                self.dfs(node)
    def hasPath(self,w):
        assert w>=0 and w<self.graph.pointer()
        return self.visited[w]
    def __path(self,w,vec):
        stack=[]
        p=w
        while p!=-1:
            stack.append(p)
            p=self.froms[p]

        while len(stack):
            vec.append(stack.pop(len(stack)-1))
    def showPath(self,w):
        vec=[]
        self.__path(w,vec)
        for i in range(len(vec)):
            print(vec[i],end="")
            if i==len(vec):
                print()
            else:
                print("--->",end="")
g1=ReadGraph().readSparseGraph('testG2.txt')
g1.show()
c1=Path(0,g1)
c1.path()
c1.showPath(6)