def mergeSort(arr):
    def splicelist(arr):
        if len(arr)>1:
            left=arr[0:len(arr)//2]
            right=arr[len(arr)//2:]
            
            splicelist(left)
            splicelist(right)
            merge(left,right,arr)
            
    def merge(left,right,arr):
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]>right[j]:
                arr[k]=right[j]
                j+=1
            else :
                arr[k]=left[i]
                i+=1
            k+=1    
        
        while (i < len(left)) :
            arr[k] = left[i]
            i+=1
            k+=1
        
        while (j < len(right)) :
            arr[k] = right[j];
            j+=1
            k+=1
    
    splicelist(arr)