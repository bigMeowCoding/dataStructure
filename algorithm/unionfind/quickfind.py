class QuickFind:
    def __init__(self,n):
        self.id=[i for i in range(n)]
        self.count=n
    def find(self,p):
        assert p>=0 and p<self.count
        return self.id[p]
    def isConnected(self,p,q):
        return self.id[p]==self.id[q]
    def unionElements(self,p,q):
        pId=self.find(p)
        qId=self.find(q)
        if pId==qId:
            return
        for i in range(self.count):
            if self.id[i]==pId:
                self.id[i]=qId
with open('largeUF.txt') as f:
    lines=f.readlines()
    quickFind=QuickFind(int(lines[0]))
    for i in range(1,len(lines)):
        p=int(lines[i].split()[0])
        q=int(lines[i].split()[1])
        quickFind.unionElements(p,q)

print(quickFind.isConnected(9,3))
print(quickFind.isConnected(0,8))
print(quickFind.isConnected(2,4))
