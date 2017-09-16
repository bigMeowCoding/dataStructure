from  algorithm.utils.util import *
class MaxHeap:

    def __init__(self,capacity):
        self.count=0
        self.data=[0 for n in range(capacity+1)]
        self.indexs = [0 for n in range(capacity + 1)]
    def size(self):
        return self.count
    def isEmpty(self):
        return self.count==0
    def insert(self,i,item):
        i+=1
        self.data[i]=item
        self.indexs[self.count+1]=i
        self.count+=1
        self.shiftUp(self.count)
    def shiftUp(self,index):
        while index>1 and self.data[self.indexs[index//2]]<self.data[self.indexs[index]]:
            swap(self.indexs,index//2,index)
            index=index//2

    def shiftDown(self,index):
        while  2*index<=self.count:
            j=2*index
            if j+1<=self.count and self.data[self.indexs[j+1]]\
                    >self.data[self.indexs[j]]:
                j+=1
            if self.data[self.indexs[index]]<self.data[self.indexs[j]]:
                swap(self.indexs,index,j)
                index=j
            else:
                break
    def extractMax(self):
        if  self.isEmpty()>0:
            raise Exception("heap is empty")
        item=self.data[self.indexs[1]]
        swap(self.indexs, 1, self.count)
        # self.data.pop(self.indexs[self.count])
        # self.indexs.pop(self.count)
        self.count-=1
        self.shiftDown(1)
        return item
    def extrackMaxIndex(self):
        if  self.isEmpty()>0:
            raise Exception("heap is empty")
        ret=self.indexs[1]-1
        swap(self.indexs, 1, self.count)
        self.count-=1
        self.shiftDown(1)
        return ret
    def getItem(self,i):
        return self.data[i+1]
    def change( self,i,item ):
        i += 1;
        self.data[i] = item
        for j in range(1,self.count+1):
            if( self.indexs[j] == i ):
                self.shiftUp(j)
                self.shiftDown(j)
                return;

if __name__=='__main__':
    heap=MaxHeap(20)
    # arr=generateUnsortedArr(0,100,20)
    arr=[2,4,1,5,6,3,5,2,5]
    for i in range(len(arr)):
        heap.insert(i,arr[i])
    heap.change(3,9)
    while heap.size():
        print(heap.extractMax())
