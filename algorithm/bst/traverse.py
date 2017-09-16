from algorithm.utils.util import *

class BST:
    class Node:
        def __init__(self,key,value):
            self.key=key
            self.value=value
            self.left=None
            self.right=None
        def cloneNode(self,node):
            self.key = node.key
            self.value = node.value
            self.left = node.left
            self.right = node.right
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
    def preorder(self):
        self.__preorder(self.root)
    def __preorder(self,node):
        if node:
            print(node.key)
            self.__preorder(node.left)
            self.__preorder(node.right)
        else:
            return

    def levelOrder(self):
        queue=[]
        queue.append(self.root)
        while len(queue)>0:
            first=queue.pop(0)
            print("\t"+str(first.value)+"\t",end="")
            if first.left:
                queue.append(first.left)
            if first.right:
                queue.append(first.right)
    def mininum(self):
        assert not self.count==0
        return self.__mininum(self.root)
    def __mininum(self,node):
        while node.left:
            return self.__mininum(node.left)
        return node
    def maxnum(self):
        assert not self.count==0
        return self.__maxnum(self.root)
    def __maxnum(self,node):
        while node.right:
            return self.__maxnum(node.right)
        return node
    def removeMin(self):
        if self.root:
           self.root=self.__removeMin(self.root)

    def __removeMin(self,node):
        if node.left==None:
            self.count-=1
            return node.right
        node.left=self.__removeMin(node.left)
        return node
    def removeMax(self):
        if self.root:
           self.root=self.__removeMax(self.root)

    def __removeMax(self,node):
        if node.right==None:
            self.count-=1
            return node.left
        node.right=self.__removeMax(node.right)
        return node
    def removeNode(self,key):
        self.__removeNode(self.root,key)
    def __removeNode(self,node,key):
        if node==None:
            return None
        if key<node.key:
            node.left=self.__removeNode(node.left,key)
            return node
        elif key>node.key:
            node.right=self.__removeNode(node.right,key)
            return node
        else:
            if node.right==None:
                self.count-=1
                return node.left
            if node.left==None:
                self.count-=1
                return node.right
            tempMiniNode=BST.Node(0,1)
            tempMiniNode.cloneNode(self.__mininum(node.right))
            tempMiniNode.right=self.__removeMin(node.right)
            tempMiniNode.left=node.left

            return  tempMiniNode

bst=BST()
# arr=generateUnsortedArr(0,100,100)
arr=[28,16,30,13,14,22,18,12,29,42]
for i in range(len(arr)):
    bst.insert(arr[i],arr[i])
bst.levelOrder()
print()
bst.removeNode(16)
bst.levelOrder()

