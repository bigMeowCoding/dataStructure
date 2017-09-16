from  algorithm.utils.util import *
class MaxHeap:
    data=[]
    count=0
    def __init__(self,arr,n):
        for i in range((n-1)//2,-1,-1):
            self.__shiftDown(arr,n,i)
        for i in range(n-1,0,-1):
            swap(arr,0,i)
            self.__shiftDown(arr,i,0)

    def size(self):
        return self.count
    def isEmpty(self):
        return self.count==0

    def __shiftDown(self,arr,n,index):
        while  2*index+1<n:
            j=2*index+1
            if j+1<n and arr[j+1]>arr[j]:
                j+=1
            if arr[index]<arr[j]:
                swap(arr,index,j)
                index=j
            else:
                break


arr=generateUnsortedArr(0,1000,100000)
heap=MaxHeap(arr,len(arr))
print(arr)