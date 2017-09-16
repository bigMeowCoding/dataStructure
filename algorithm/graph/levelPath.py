from algorithm.utils.readGraph import ReadGraph
class levelPath:
    def __init__(self,s,graph):
        self.visited=[False for i in range(graph.pointer())]
        assert s>=0 and s<graph.pointer()
        self.s=s
        self.graph=graph
        self.froms= [-1 for i in range(graph.pointer())]
        self.ord=[-1 for i in range(graph.pointer())]
    def path(self):
        queue=[]
        queue.append(self.s)
        self.visited[self.s]=True
        self.ord[self.s]=0
        while len(queue)>0:
            v=queue.pop(0)
            iter = self.graph.adjIterator(self.graph, v)
            while not iter.end():
                node = iter.next()
                if not self.visited[node]:
                    self.froms[node] = v
                    self.visited[node] = True
                    self.ord[node]=self.ord[v]+1
                    queue.append(node)

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
            if i==len(vec)-1:
                print()
            else:
                print("--->",end="")
if __name__=="__main__":
    g1=ReadGraph().readSparseGraph('testG2.txt')
    g1.show()
    c1=levelPath(0,g1)
    c1.path()
    c1.showPath(4)