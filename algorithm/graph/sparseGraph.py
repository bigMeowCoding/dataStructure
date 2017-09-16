import random

from algorithm.utils.readGraph import ReadGraph

class SparseGraph:
    def __init__(self, n, directed):
        self.n = n
        self.m = 0
        self.directed = directed
        self.g = []
        for i in range(n):
            self.g.append([])

    def pointer(self):
        return self.n

    def edge(self):
        return self.m

    def addEdge(self, v, w):
        assert v >= 0 and v < self.n
        assert w >= 0 and w < self.n
        if self.hasEdge(v, w):
            return
        self.g[v].append(w)
        if not self.directed and not v==w:
            self.g[w].append(v)
        self.m += 1

    def hasEdge(self, v, w):
        assert v >= 0 and v < self.n
        assert w >= 0 and w < self.n
        for i in range(len(self.g[v])):
            if self.g[v][i]==w:
                return True
        return False
    def show(self):
        for i in range(self.pointer()):
            print(str(i)+"\t:",end="")
            for j in range(len(self.g[i])):
                print("\t"+str(self.g[i][j]),end="")
            print()
    class adjIterator:
        def __init__(self,graph,v):
            self.graph=graph
            self.v=v
            self.index=0

        def next(self):
            temp=self.graph.g[self.v][self.index]
            self.index+=1
            return temp
        def end(self):
            return self.index>=len(self.graph.g[self.v])
# sparseGraph=SparseGraph(100,False)
# edge=100
# for i in range(edge):
#     sparseGraph.addEdge(random.randint(0,99),random.randint(0,99))
# for i in range(sparseGraph.pointer()):
#     ite=SparseGraph.adjIterator(sparseGraph,i)
#     print("pointer\t" + str(i) + "\tedge:", end="")
#     while not ite.end():
#
#         print(str(ite.next())+"\t",end="")
#     print()
if __name__=="__main__":
    g1=ReadGraph().readSparseGraph('testG1.txt')
    g1.show()
