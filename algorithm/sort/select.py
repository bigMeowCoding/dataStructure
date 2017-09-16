from algorithm.utils import util
class SelectSort:
    def selectSort(self,arr,n):
        for i in range(n):
            for j in range(i+1,n):
                if arr[j]<arr[i]:
                    self.swap(arr,i,j)
    def swap(self,arr,i,j):
        temp=arr[i]
        arr[i]=arr[j]
        arr[j]=temp

sort=SelectSort()
arr=util.generateUnsortedArr(0,10000,100)
sort.selectSort(arr,len(arr))
print(arr)