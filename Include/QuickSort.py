import time;
import linecache

def quicksort(arr):
    less = []
    equal = []
    greater = []

    if len(arr) > 1:

        pivot = arr[0]

        for x in arr:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)

        return quicksort(less) + equal + quicksort(greater)
    else:
        return arr


#arr = open('InOrder', "r")
arr = open('Reverse', "r")
#arr = open('RandomNumbers', "r")
arr = arr.readlines()
quicksort(arr)
print(time.perf_counter())
