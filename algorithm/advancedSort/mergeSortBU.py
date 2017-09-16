from algorithm.utils import util


class MergeBU:
    def mergeSort(self,arr,n):
        sz=1
        while sz<=n:
            i=0
            while i+sz<n:
                self.__merge(arr,i,i+sz-1,min(i+sz+sz-1,n-1))
                i+=sz+sz
            sz += sz
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

sort = MergeBU()
arr = util.generateUnsortedArr(0, 100, 100000)
sort.mergeSort(arr, len(arr))
print(arr)
