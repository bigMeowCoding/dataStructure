from  algorithm.utils.util import *
class MinHeap:
    def __init__(self,capacity):
        self.data=[0 for n in range(capacity+2)]
        self.count=0
        self.capacity=capacity
    def size(self):
        return self.count
    def isEmpty(self):
        return self.count==0
    def insert(self,item):
        if self.count>=self.capacity//2:
            self.resizeToBig(self.capacity*2)
        self.data[self.count+1]=item
        self.count+=1
        self.shiftUp(self.count)
    def resizeToSmall(self,size):
        newData=[0 for i in range(size+2)]
        for i in range(1,len(newData)):
            newData[i]=self.data[i]
        self.data=newData
        self.capacity=size

    def resizeToBig(self, size):
            newData = [0 for i in range(size + 2)]
            for i in range(1, len(self.data)):
                newData[i] = self.data[i]
            self.data = newData
            self.capacity = size
    def shiftUp(self,index):
        while index>1 and self.data[index//2]>self.data[index]:
            swap(self.data,index//2,index)
            index=index//2
    def shiftDown(self,index):
        while  2*index<=self.count:
            j=2*index
            if j+1<=self.count and self.data[j+1]<self.data[j]:
                j+=1
            if self.data[index]>self.data[j]:
                swap(self.data,index,j)
                index=j
            else:
                break
    def extractMin(self):
        if  self.isEmpty()>0:
            raise Exception("heap is empty")

        item=self.data[1]
        swap(self.data, 1, self.count)
        self.data.pop(self.count)
        self.count-=1
        self.shiftDown(1)
        if self.count < self.capacity // 2:
            self.resizeToSmall(self.capacity // 2)
        return item
if __name__=='__main__':
    heap=MinHeap(1)
    arr=generateUnsortedArr(0,100,100)
    for i in range(len(arr)):
        heap.insert(arr[i])
    while heap.size():
        print(heap.extractMin())