

class ReadGraph:
    def readSparseGraph(self,fileName):
        from algorithm.graph.sparseGraph import SparseGraph
        with open(fileName) as f:
            s1=f.readline()
            n=int(s1.split()[0])

            g1=SparseGraph(n,False)
            tempLine = f.readline()
            while tempLine:
                p1=int(tempLine.split()[0])
                p2=int(tempLine.split()[1])
                g1.addEdge(p1,p2)
                tempLine=f.readline()
            return g1

    def readDenseGraph(self,fileName):
        from algorithm.graph.denseGraph import DenseGraph
        with open(fileName) as f:
            s1=f.readline()
            n=int(s1.split()[0])

            g1=DenseGraph(n,False)
            tempLine = f.readline()
            while tempLine:
                p1=int(tempLine.split()[0])
                p2=int(tempLine.split()[1])
                g1.addEdge(p1,p2)
                tempLine=f.readline()
            return g1
    def readWeightDenseGraph(self,fileName):
        from algorithm.weightGraph.denseGraph import DenseGraph
        with open(fileName) as f:
            s1=f.readline()
            n=int(s1.split()[0])

            g1=DenseGraph(n,False)
            tempLine = f.readline()
            while tempLine:
                p1=int(tempLine.split()[0])
                p2=int(tempLine.split()[1])
                w=float(tempLine.split()[2])
                g1.addEdge(p1,p2,w)
                tempLine=f.readline()
            return g1
    def readWidthSparseGraph(self,fileName):
        from algorithm.weightGraph.sparseGraph import SparseGraph
        with open(fileName) as f:
            s1=f.readline()
            n=int(s1.split()[0])

            g1=SparseGraph(n,True)
            tempLine = f.readline()
            while tempLine:
                p1=int(tempLine.split()[0])
                p2=int(tempLine.split()[1])
                weight = float(tempLine.split()[2])
                g1.addEdge(p1,p2,weight)
                tempLine=f.readline()
            return g1