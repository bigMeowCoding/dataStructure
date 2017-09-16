from  algorithm.heap.minHeap import MinHeap

class LayPrim:
    def __init__(self,graph):
        self.graph=graph
        pointers=graph.pointer()
        self.marked=[False for i in range(pointers)]
        self.mstWeight=0
        self.mst=[]
        self.uf=UnionFind()
        self.heap=MinHeap(pointers)
    def visited(self,v):
        from algorithm.weightGraph.sparseGraph import SparseGraph
        assert v>=0 and v<self.graph.pointer()
        self.marked[v]=True
        iter=SparseGraph.adjIterator(self.graph,v)
        while not iter.end():
            w=iter.next()
            if not self.marked[w.other(v)]:
                self.heap.insert(w)

    def layPrim(self):
        self.visited(0)
        while self.heap.size()>0:
            temp=self.heap.extractMin()
            if self.marked[temp.v()]==self.marked[temp.w()]:
                continue
            self.mst.append(temp)
            if(not self.marked[temp.v()]):
                self.visited(temp.v())
            if (not self.marked[temp.w()]):
                self.visited(temp.w())
        self.mstWeight=self.mst[0].weightValue()
        for i in range(1,len(self.mst)):
            self.mstWeight+=self.mst[i].weightValue()
    def result(self):
        return self.mstWeight
    def mstEdges(self):
        return self.mst
if __name__=="__main__":
    g1=ReadGraph().readWidthSparseGraph('testG1.txt')
    prim=LayPrim(g1)
    prim.layPrim()
    edges=prim.mstEdges()
    for edge in edges:
        print(str(edge.v())+"-->"+str(edge.w())+":"+str(edge.weightValue()))
    print(prim.result())
