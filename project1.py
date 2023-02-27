import sys
sys.setrecursionlimit(100000) #for high range of recursion

#linear search
def lsearch(l,x):
    for i in range(0,len(l)):
        if l[i]==x:
            return True
    else:
        return False
#time complexity is O(n)   
        


#Binary Search
def bsearch(seq,v,l,r):
    if(r-l==0):
        return False
    mid=(l+r)//2
    if(v==seq[mid]):
        return True
    if(v<seq[mid]):
        return bsearch(seq,v,l,mid)
    else:
        return bsearch(seq,v,mid+1,r)
#Time complexity is O(logn) the necessary condition is the list has to be sorted before performing search.    

#Selectionsort
def selectionsort(l):
    for start in range(len(l)):
        minpos=start
        for i in range(start,len(l)):
            if l[i]<l[minpos]:
                minpos=i
        (l[start],l[minpos])=(l[minpos],l[start])
    return l   
#Time complexity is O(n^2), Time complexity is same for all the cases.space is O(1)

#insertionSort 
def InsertionSort(seq):
    for sliceEnd in range(len(seq)):
        pos=sliceEnd
        while pos>0 and seq[pos]<seq[pos-1]:
            (seq[pos],seq[pos-1])=(seq[pos-1],seq[pos])
            pos=pos-1
    return seq   
#Time complexity is O(n^2) best case is O(n) is case of sorted list. space is O(1)



#merge sort
def merge(A,B):
    (c,m,n)=([],len(A),len(B))
    (i,j)=(0,0)
    while i+j<m+n:
        if i==m:
            c.append(B[j])
            j+=1
        elif j==n:
            c.append(A[i])
            i+=1
        elif A[i]<=B[j]:
            c.append(A[i])
            i+=1
        elif A[i]> B[j]:
            c.append(B[j])
            j+=1
    return c

def mergesort(A,left,right):
    if right-left<=1:
        return A[left:right]
    if right-left >1:
        mid=(left+right)//2
        l=mergesort(A,left,mid)
        r=mergesort(A,mid,right)
        return merge(l,r)


#time complexity is O(nlogn) best for large range sorting, Time complexity is same for all cases.
#space is O(n)

#QuickSort
def quicksort(A,l,r):
    if r-l<=1:
        return ()
    yellow=l+1
    for green in range(l+1,r):
        if A[green]<=A[l]:
            (A[yellow],A[green])=(A[green],A[yellow])
            yellow+= 1
    (A[l],A[yellow-1])=(A[yellow-1],A[l])
    quicksort(A,l,yellow-1)
    quicksort(A,yellow,r)
    return A
#Time complexity is O(nlogn) the problem is same as the insersion sort..,worst case time complexity is O(n^2)
#space is O(n)