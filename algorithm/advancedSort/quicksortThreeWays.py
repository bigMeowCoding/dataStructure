import random

from algorithm.utils import util
from algorithm.utils.util import swap

class QuickSort3way:
    def quickSort(self,arr,n):
        self.__quickSortThreeWays(arr,0,n-1)
    def __quickSortThreeWays(self,arr,l,r):
        if(l>=r):
            return
        radomIndex = random.randint(l,r)
        swap(arr, l, radomIndex)
        temp = arr[l]
        lt= l
        gt= r+1
        i=l+1
        while i<gt:
            if(arr[i]<temp):
               swap(arr,i,lt+1)
               lt+=1
               i+=1
            elif(arr[i]>temp):
                swap(arr,gt-1,i)
                gt-=1
            else:
                i+=1
        swap(arr,l,lt)
        self.__quickSortThreeWays(arr,l,lt-1)
        self.__quickSortThreeWays(arr,gt,r)
sort=QuickSort3way()
arr=util.generateUnsortedArr(0,1000,100000)
sort.quickSort(arr,len(arr))
print(arr)
