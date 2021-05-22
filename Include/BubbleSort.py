import time
import linecache

def bubbleSort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp




#arr = open('InOrder', "r")
arr = open('Reverse', "r")
#arr = open('RandomNumbers', "r")
arr = arr.readlines()
bubbleSort(arr)
print(time.perf_counter())


