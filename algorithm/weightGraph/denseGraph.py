import random

from algorithm.utils.readGraph import ReadGraph
from  algorithm.weightGraph.Edge import Edge

class DenseGraph:
    def __init__(self,n,directed):
        self.n=n
        self.m=0
        self.directed=directed
        self.g=[]
        for i in range(n):
            self.g.append([None for i in range(n)])

    def pointer(self):
        return self.n
    def edge(self):
        return  self.m

    def addEdge(self,v,w,weight):
        assert v>=0 and v<self.n
        assert w>=0 and w<self.n
        if self.hasEdge(v,w):
            self.g[v][w]=None
            if not self.directed:
                self.g[w][v]=None
            self.m-=1

        self.g[v][w]=Edge(v,w,weight)
        if not self.directed:
            self.g[w][v]=Edge(w,v,weight)
        self.m+=1

    def hasEdge(self,v,w):
        assert v>=0 and v<self.n
        assert w>=0 and w<self.n
        return not self.g[v][w]==None
    def show(self):
        for i in range(self.pointer()):
            print(str(i)+"\t:",end="")
            for j in range(len(self.g[i])):
                temp=self.g[i][j]
                if temp:
                    print("\t"+str(temp.weightValue())+"\t",end="")
                else:
                    print("\tNone\t", end="")
            print()
    class adjIterator:
        def __init__(self,graph,v):
            self.graph=graph
            self.v=v
            self.index=0

        def next(self):
            for i in range(self.index,self.graph.pointer()):
                if  self.graph.g[self.v][i]:
                    temp=self.graph.g[self.v][i].weight()
                    self.index+=1
                    return temp
                else:
                    self.index += 1

        def end(self):
            return self.index>=self.graph.pointer()
if __name__=="__main__":
    dense=ReadGraph().readWeightDenseGraph("testG1.txt")
    dense.show()