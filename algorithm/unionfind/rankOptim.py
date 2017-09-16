class UnionFind:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.count=n
        self.rank=[1 for i in range(n)]
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
        if self.rank[pRoot]>self.rank[qRoot]:
            self.parent[qRoot]=pRoot

        elif self.rank[pRoot]<self.rank[qRoot]:
            self.parent[pRoot] = qRoot
        else:
            self.parent[pRoot] = qRoot
            self.rank[qRoot]+=1
            
with open('largeUF.txt') as f:
    lines=f.readlines()
    quickFind=UnionFind(int(lines[0]))
    for i in range(1,len(lines)):
        p=int(lines[i].split()[0])
        q=int(lines[i].split()[1])
        quickFind.unionElements(p,q)