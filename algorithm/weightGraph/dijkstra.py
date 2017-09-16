from algorithm.heap.IndexMInheap import IndexMinHeap
from algorithm.utils.readGraph import ReadGraph
from algorithm.weightGraph.sparseGraph import SparseGraph
class Dijkstra:
    def __init__(self,graph,s):
        self.graph=graph
        self.s=s
        self.pointer=graph.pointer()
        self.disTo=[-1 for i in range(self.pointer)]
        self.marked=[None for i in range(self.pointer)]
        self.fromTo=[None for i in range(self.pointer)]
        self.imp=IndexMinHeap(self.pointer)
    def djkstra(self):
        self.disTo[self.s]=0
        self.imp.insert(self.s,self.disTo[self.s])
        self.marked[self.s]=True
        while not self.imp.size()==0:
            v=self.imp.extrackMinIndex()
            self.marked[v]=True
            ite=SparseGraph.adjIterator(self.graph,v)
            while not ite.end():
                edge=ite.next()
                w=edge.other(v)
                if not self.marked[w]:
                    if self.fromTo[w]==None or self.disTo[w]>self.disTo[v]+edge.weightValue():
                        self.fromTo[w]=edge
                        self.disTo[w]=self.disTo[v]+edge.weightValue()
                        if self.imp.hasIndex(w):
                            self.imp.change(w,self.disTo[w])
                        else:
                            self.imp.insert(w,self.disTo[w])

    def shortestPathTo(self,w):
        return self.disTo[w]
    def hasPath(self,w):
        assert w>=0 and w<self.graph.pointer()
        return not self.marked[w]==None
    def shortestPath(self,w,vec):
        stack=[]
        edge=self.fromTo[w]
        v=edge.other(w)
        while not v==self.s:
            stack.append(edge)
            edge=self.fromTo[v]
            v=edge.other(v)
        stack.append(edge)
        while len(stack):
            vec.append(stack.pop(len(stack)-1))
    def showPath(self,w):
        vec=[]
        self.shortestPath(w,vec)
        for i in range(len(vec)):
            if i==len(vec)-1:
                print(str(vec[i].v())+"--->"+str(vec[i].w()))
            else:
                print(str(vec[i].v())+"--->",end="")

if __name__=="__main__":
    g1=ReadGraph().readWidthSparseGraph('testG1.txt')

    dijkstra=Dijkstra(g1,1)
    dijkstra.djkstra()
    print(dijkstra.hasPath(2))

        # dijkstra.showPath(2)
    dijkstra=Dijkstra(g1,0)
    dijkstra.djkstra()
    dijkstra.showPath(2)
    dijkstra=Dijkstra(g1,0)
    dijkstra.djkstra()
    dijkstra.showPath(3)
    dijkstra=Dijkstra(g1,0)
    dijkstra.djkstra()
    dijkstra.showPath(4)