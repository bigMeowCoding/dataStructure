from algorithm.heap.IndexMInheap import IndexMinHeap
from algorithm.utils.readGraph import ReadGraph
from algorithm.weightGraph.sparseGraph import SparseGraph
class BellmanFord:
    def __init__(self,graph,s):
        self.graph=graph
        self.s=s
        pointer=graph.pointer()
        self.pointer=pointer
        self.fromTo=[None for _ in range(pointer)]
        self.negativeCycle=False
        self.disTo=[0 for _ in range(pointer)]
        self.imp=IndexMinHeap(pointer)
    def bellManFord(self):
        self.disTo[self.s] = 0
        self.imp.insert(self.s, self.disTo[self.s])

        for i in range(1,self.pointer):
            for j in range(self.pointer):
                ite = SparseGraph.adjIterator(self.graph, j)
                while not ite.end():
                    edge = ite.next()
                    if self.fromTo[edge.w()] == None or self.disTo[edge.w()] >self.disTo[edge.v()] + edge.weightValue():
                        self.fromTo[edge.w()] = edge
                        self.disTo[edge.w()] = self.disTo[edge.v()] + edge.weightValue()
        self.negativeCycle=self.detectNegativeCycle()
    def detectNegativeCycle(self):
        for j in range(self.pointer):
            ite = SparseGraph.adjIterator(self.graph, j)
            while not ite.end():
                edge = ite.next()
                if self.fromTo[edge.w()] == None or self.disTo[edge.w()] > self.disTo[edge.v()] + edge.weightValue():
                    return True
        return False
    def hasNegativeCycle(self):
        return self.negativeCycle
    def shortestPathTo(self, w):
        return self.disTo[w]

    def hasPath(self, w):
        assert w >= 0 and w < self.graph.pointer()
        return not self.marked[w] == None

    def shortestPath(self, w, vec):
        stack = []
        edge = self.fromTo[w]
        v = edge.other(w)
        while not v == self.s:
            stack.append(edge)
            edge = self.fromTo[v]
            v = edge.other(v)
        stack.append(edge)
        while len(stack):
            vec.append(stack.pop(len(stack) - 1))

    def showPath(self, w):
        vec = []
        self.shortestPath(w, vec)
        for i in range(len(vec)):
            if i == len(vec) - 1:
                print(str(vec[i].v()) + "--->" + str(vec[i].w()))
            else:
                print(str(vec[i].v()) + "--->", end="")

if __name__ == "__main__":
    # g1 = ReadGraph().readWidthSparseGraph('testG2_negative_circle.txt')
    g1 = ReadGraph().readWidthSparseGraph('testG2.txt')
    bellmanFord = BellmanFord(g1, 0)
    bellmanFord.bellManFord()
    if bellmanFord.hasNegativeCycle():
        print("has negative cycle")
    else:
        bellmanFord.showPath(2)
    bellmanFord = BellmanFord(g1, 0)
    bellmanFord.bellManFord()
    if bellmanFord.hasNegativeCycle():
        print("has negative cycle")
    else:
        bellmanFord.showPath(1)
    bellmanFord = BellmanFord(g1, 0)
    bellmanFord.bellManFord()
    if bellmanFord.hasNegativeCycle():
        print("has negative cycle")
    else:
        bellmanFord.showPath(3)
    bellmanFord = BellmanFord(g1, 0)
    bellmanFord.bellManFord()
    if bellmanFord.hasNegativeCycle():
        print("has negative cycle")
    else:
        bellmanFord.showPath(4)
