import random

from algorithm.utils import util
from algorithm.utils.util import swap

class QuickSort:
    def quickSort(self,arr,n):
        self.__quickSort(arr,0,n-1)
    def __quickSort(self,arr,l,r):
        if(l>=r):
            return
        position=self.__partition(arr,l,r)
        self.__quickSort(arr,l,position-1)
        self.__quickSort(arr,position+1,r)
    def __partition(self,arr,l,r):
        radomIndex=random.randint(l,r)
        swap(arr,l,radomIndex)
        temp=arr[l]
        j=l
        for i in range(l+1,r+1):
            if(arr[i]<temp):
                j+=1
                swap(arr,j,i)
        swap(arr,j,l)
        return j
sort=QuickSort()
arr=util.generateUnsortedArr(0,1000,100000)
sort.quickSort(arr,len(arr))
print(arr)
