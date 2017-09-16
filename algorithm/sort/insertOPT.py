from algorithm.utils import util


class InsertSort:
    def insertSort(self, arr, n):
        for i in range(1, n):
            temp = arr[i]
            j=i
            while j>0 and  temp < arr[j - 1]:
                arr[j]=arr[j-1]
                j-=1
            arr[j]=temp
    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp


sort = InsertSort()
arr = util.generateUnsortedArr(0, 10000, 10000)
sort.insertSort(arr, len(arr))
print(arr)