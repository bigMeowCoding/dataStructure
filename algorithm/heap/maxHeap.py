from  algorithm.utils.util import *
class MaxHeap:

    count=0
    def __init__(self,capacity):
        self.data=[0 for n in range(capacity+1)]
    def size(self):
        return self.count
    def isEmpty(self):
        return self.count==0
    def insert(self,item):
        self.data[self.count+1]=item
        self.count+=1
        self.shiftUp(self.count)
    def shiftUp(self,index):
        while index>1 and self.data[index//2]<self.data[index]:
            swap(self.data,index//2,index)
            index=index//2
    def shiftDown(self,index):
        while  2*index<=self.count:
            j=2*index
            if j+1<=self.count and self.data[j+1]>self.data[j]:
                j+=1
            if self.data[index]<self.data[j]:
                swap(self.data,index,j)
                index=j
            else:
                break
    def extractMax(self):
        if  self.isEmpty()>0:
            raise Exception("heap is empty")
        item=self.data[1]
        swap(self.data, 1, self.count)
        self.data.pop(self.count)
        self.count-=1
        self.shiftDown(1)
        return item

heap=MaxHeap(20)
arr=generateUnsortedArr(0,100,20)
for i in range(len(arr)):
    heap.insert(arr[i])
while heap.size():
    print(heap.extractMax())
print(str(1.2))