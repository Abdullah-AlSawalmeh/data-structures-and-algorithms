# Merge Sort

Merge Sort is a Divide and Conquer algorithm. It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves. 

## Problem Domain:
Write a function that implements the Merge sort algorithm, where the input is a list and the output is the sorted list.

## Algorithm
To sort an array of size n in ascending order:


1. Find the middle point to divide the array into two halves.

2. Call mergeSort for first half 

3. Call mergeSort for second half.
4. Merge the two halves sorted in step 2 and 3

## Pseudo Code:
```
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length
           
    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1
            
        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
```

## Trace (Visual):
#### Input: [8,4,23,42,16,15]
![](merge_sort_article1.png)
![](merge_sort_article2.png)


## Time Complexity:
`θ(nLogn)`, as it always divides the array into two halves and takes linear time to merge two halves.
