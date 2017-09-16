class UnionFind:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.count=n

    def find(self,p):
        assert p>=0 and p<self.count
        while p!=self.parent[p]:
            p=self.parent[p]
        return p

    def isConnected(self,p,q):
        return self.find(p)==self.find(q)

    def unionElements(self,p,q):
        pRoot=self.find(p)
        qRoot=self.find(q)
        if pRoot==qRoot:
            return
        self.parent[pRoot]=qRoot