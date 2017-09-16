from  algorithm.heap.IndexMInheap import IndexMinHeap
from algorithm.utils.readGraph import ReadGraph


class LayPrimOPT:
    def __init__(self,graph):
        self.graph=graph
        pointers=graph.pointer()
        self.marked=[False for i in range(pointers)]
        self.edgeTo=[None for i in range(pointers)]
        self.mstWeight=0
        self.mst=[]
        self.heap=IndexMinHeap(pointers)
    def visited(self,v):
        from algorithm.weightGraph.sparseGraph import SparseGraph
        assert v>=0 and v<self.graph.pointer()
        self.marked[v]=True
        iter=SparseGraph.adjIterator(self.graph,v)
        while not iter.end():
            edge=iter.next()
            w=edge.other(v)
            if not self.marked[w]:
                if not self.edgeTo[w]:
                    self.edgeTo[w]=edge
                    self.heap.insert(w,edge.weightValue())
                elif edge.weightValue()<self.edgeTo[w].weightValue():
                    self.edgeTo[w]=edge
                    self.heap.change(w,edge.weightValue())

    def prim(self):
        self.visited(0)
        while self.heap.size()>0:
            temp=self.heap.extrackMinIndex()
            self.mst.append(self.edgeTo[temp])
            self.visited(temp)
        self.mstWeight=self.mst[0].weightValue()
        for i in range(1,len(self.mst)):
            self.mstWeight+=self.mst[i].weightValue()
    def result(self):
        return self.mstWeight
    def mstEdges(self):
        return self.mst
if __name__=="__main__":
    g1=ReadGraph().readWidthSparseGraph('testG4.txt')
    prim=LayPrimOPT(g1)
    prim.prim()
    edges=prim.mstEdges()
    for edge in edges:
        print(str(edge.v())+"-->"+str(edge.w())+":"+str(edge.weightValue()))
    print(prim.result())
