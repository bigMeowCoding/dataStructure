from algorithm.utils import util


class Merge:
    def mergeSort(self,arr,n):
        self.__mergeSort(arr,0,n-1)
    def __mergeSort(self,arr,l,r):
        if(r<=l):
            return
        mid=l+(r-l)//2
        self.__mergeSort(arr,l,mid)
        self.__mergeSort(arr,mid+1,r)
        if arr[mid]>arr[mid+1]:
            self.__merge(arr,l,mid,r)
    def __merge(self,arr,l,mid,r):
        aux=[]
        for i in range(l,r+1):
            aux.append(arr[i])
        i=l
        j=mid+1
        for index in range(l,r+1):
            if i>mid:
                arr[index]=aux[j-l]
                j+=1
            elif j>r:
                arr[index]=aux[i-l]
                i+=1
            elif aux[i-l]>aux[j-l]:
                arr[index]=aux[j-l]
                j+=1
            else:
                arr[index]=aux[i-l]
                i+=1

sort = Merge()
arr = util.generateUnsortedArr(0, 10000, 100000)
sort.mergeSort(arr, len(arr))
print(arr)