class Edge:
    def __init__(self,a,b,weight):
        self.a=a
        self.b=b
        self.weight=weight

    def v(self):
        return self.a
    def w(self):
        return self.b
    def weightValue(self):
        return self.weight
    def other(self,x):
        assert x==self.a or x==self.b
        if x==self.a:
            return self.b
        else:
            return self.a
    def __lt__(self, other):
        return self.weight<other.weight