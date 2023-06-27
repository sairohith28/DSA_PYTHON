def swap(a,b,arr):
    tmp=arr[a]
    arr[a]=arr[b]
    arr[b]=tmp
def partition(arr,start,end):
    pi=start
    pivot=arr[pi]
    while start<end:
        while start<len(arr) and arr[start]<=pivot:
            start+=1
        while arr[end]>pivot:
            end-=1
        if start<end:
            swap(start,end,arr)
        print(arr)
    swap(pi,end,arr)
    return end
def qs(arr,start,end):
    if start<end:
        pi=partition(arr,start,end)
        qs(arr,start,pi-1)
        qs(arr,pi+1,end)
arr=[11,8,34,5,12]
qs(arr,0,len(arr)-1)
print(arr)