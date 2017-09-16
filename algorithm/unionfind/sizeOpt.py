class UnionFind:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.count=n
        self.sz=[1 for i in range(n)]
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
        if self.sz[pRoot]>self.sz[qRoot]:
            self.parent[qRoot]=pRoot
            self.sz[pRoot]+=self.sz[qRoot]
        else:
            self.parent[pRoot] = qRoot
            self.sz[qRoot]+=self.sz[pRoot]
if __name__=="__main__":
    with open('largeUF.txt') as f:
        lines=f.readlines()
        quickFind=UnionFind(int(lines[0]))
        for i in range(1,len(lines)):
            p=int(lines[i].split()[0])
            q=int(lines[i].split()[1])
            quickFind.unionElements(p,q)

    print(quickFind.isConnected(9,3))
    print(quickFind.isConnected(0,8))
    print(quickFind.isConnected(2,14))
    print(quickFind.isConnected(786321,1521))