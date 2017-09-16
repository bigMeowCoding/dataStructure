from algorithm.utils import util


class InsertSort:
    def insertSort(self,arr,n):
        for i in range(1,n):
            for j in range(i,0,-1):
                if(arr[j]<arr[j-1]):
                    self.swap(arr,j,j-1)
                else:
                    break

    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
sort=InsertSort()
arr=util.generateUnsortedArr(0,100,10000)
sort.insertSort(arr,len(arr))
print(arr)