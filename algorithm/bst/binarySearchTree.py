class BST:
    class Node:
        def __init__(self,key,value):
            self.key=key
            self.value=value
            self.left=None
            self.right=None

    def __init__(self):
        self.root=None
        self.count=0
    def size(self):
        return self.count
    def isEmpty(self):
        return self.count==0
    def insert(self,key,value):
        self.root=self.__insert(self.root,key,value)
    def __insert(self,node,key,value):
        if node==None:
            self.count+=1
            return BST.Node(key,value)
        if(key==node.key):
            node.value=value
            return node
        elif node.key<key:
            node.right=self.__insert(node.right,key,value)
            return node
        elif node.key>key:
            node.left=self.__insert(node.left,key,value)
            return node
    def contain(self,key):
        return self.__contain(self.root,key)
    def __contain(self,node,key):
        if node==None:
            return False
        if key==node.key:
            return True
        elif key<node.key:
            return self.__contain(node.left,key)
        elif key>node.key:
            return self.__contain(node.right,key)
    def search(self,key):
        return  self.__search(self.root,key)
    def __search(self,node,key):
        if node==None:
            return None
        if isinstance(key,str):
            if key.lower() == node.key.lower():
                return node.value
            elif key.lower() < node.key.lower():
                return self.__search(node.left, key)
            elif key.lower() > node.key.lower():
                return self.__search(node.right, key)
        else:
            if key==node.key:
                return node.value
            elif key<node.key:
                return self.__search(node.left,key)
            elif key>node.key:
                return self.__search(node.right,key)

bst=BST()
with open('bible.txt') as f:
    lines=f.readlines()
    words=[line.split() for line in lines]
    for i in range(len(words)):
        for j in range(len(words[i])):
            ref = bst.search(words[i][j])
            if ref:
                ref += 1
                bst.insert(words[i][j], ref)
            else:
                bst.insert(words[i][j], 1)
print(bst.search('God'))