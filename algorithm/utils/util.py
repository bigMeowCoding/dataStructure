import random
def generateUnsortedArr(l,g,n):
    result=[]
    for i in range(n):
        result.append(random.randint(l,g))
    return  result

def swap(arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp