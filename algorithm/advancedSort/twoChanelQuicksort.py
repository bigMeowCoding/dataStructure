import random

from algorithm.utils import util
from algorithm.utils.util import swap

class QuickSortTwoChanel:
    def quickSort(self,arr,n):
        self.__quickSort(arr,0,n-1)
    def __quickSort(self,arr,l,r):
        if(l>=r):
            return
        position=self.__partition2(arr,l,r)
        self.__quickSort(arr,l,position-1)
        self.__quickSort(arr,position+1,r)
    def __partition2(self,arr,l,r):
        radomIndex=random.randint(l,r)
        swap(arr,l,radomIndex)
        temp=arr[l]
        i=l+1
        j=r
        while True:
            while i<=r and arr[i]<temp:
                i+=1
            while j>=l+1 and arr[j]>temp :
                j-=1
            if i>j:
                break
            swap(arr,i,j)
            i+=1
            j-=1
        swap(arr,j,l)
        return j
sort=QuickSortTwoChanel()
arr=util.generateUnsortedArr(0,1000,100000)
sort.quickSort(arr,len(arr))
print(arr)
