from algorithm.heap.minHeap import MinHeap
from algorithm.unionfind.sizeOpt import UnionFind
from algorithm.utils.readGraph import ReadGraph


class Kruskal:
    def __init__(self,graph):
        self.graph=graph
        self.mstWeight=0
        self.mst=[]
        self.heap=MinHeap(graph.pointer())
        self.uf=UnionFind(graph.pointer())
    def KruskalMST(self):
        from algorithm.weightGraph.sparseGraph import SparseGraph
        for i in range(self.graph.pointer()):
            ite=SparseGraph.adjIterator(self.graph,i)
            while not ite.end():
                temp=ite.next()
                if temp.v()<temp.w():
                    self.heap.insert(temp)
        while self.heap.size()>0 and len(self.mst)<self.graph.pointer()-1:
            edge=self.heap.extractMin()
            if self.uf.isConnected(edge.v(),edge.w()):
                continue
            self.mst.append(edge)
            self.uf.unionElements(edge.v(),edge.w())
        self.mstWeight=self.mst[0].weightValue()
        for i in range(1,len(self.mst)):
            self.mstWeight+=self.mst[i].weightValue()
    def result(self):
        return self.mstWeight
    def mstEdges(self):
        return self.mst
if __name__=="__main__":
    g1=ReadGraph().readWidthSparseGraph('testG4.txt')
    kruskal=Kruskal(g1)
    kruskal.KruskalMST()
    edges=kruskal.mstEdges()
    for edge in edges:
        print(str(edge.v())+"-->"+str(edge.w())+":"+str(edge.weightValue()))
    print(kruskal.result())