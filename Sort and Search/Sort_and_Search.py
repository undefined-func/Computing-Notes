#!/usr/bin/env python
# coding: utf-8

# # Sort Algorithms
# 
# Implement sort algorithms.
# 
# *   Insertion sort
# *   Bubble sort
# *   Quicksort
# *   Merge sort
# 
# 

# In[1]:


#Run this cell first to generate test data.
from random import randint
test = [randint(1, 50) for i in range(10)]
test


# In[4]:


#Or copy and paste a list into this cell (and run).
test = 


# ## Bubble Sort
# 
# Worst-case time complexity: $O(n^{2})$
# 
# ### Notes
# After the $n$th pass, the last $n$ elements are bubbled up in place.
# 
# ### Algorithm
# 
# 1.   Starting with the first element, compare the current element with the next element.
# 2.   If current element > next element, do a swap.
# 3.   Assign current element to next element.
# 4.   Repeat steps 1-3 for the first $n$ element for the $n$th pass.
# 5.   Sorting is complete when there is no swaps in a pass.
# 
# 

# In[2]:


def bubble_sort(arr):
    exchanges = True
    pass_no = len(arr) - 1
    while pass_no > 0 and exchanges:
        exchanges = False
        for i in range(pass_no):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                exchanges = True
        pass_no -= 1
    return arr


# In[3]:


def recursive_bubble_sort(arr):
    if len(arr) == 1:
        return arr
    else:
        swap = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                swap = True
        if swap == False:
            return arr
        else:
            return recursive_bubble_sort(arr[:-1]) + [arr[-1]]


# In[4]:


bubble_sort(test)


# In[5]:


recursive_bubble_sort(test)


# ## Insertion sort
# 
# Worst-case time complexity: $O(n^{2})$
# 
# ### Notes
# A sorted portion of the array is maintained on the left-hand side. The first element is sorted.
# 
# ### Algorithm
# 
# 1.   Starting with the second element, compare with the elements in the sorted sub-array.
# 2.   Shift all the elements that are greater than the current element one position to the right.
# 3.   Insert the element.
# 4.   Repeat steps 1-3 for all elements.
# 
# 

# In[6]:


def insertion_sort(arr):
    for i in range(1, len(arr)):
        
        #element to be compared
        key = arr[i]
        position = i
        
        #Move elements of arr[0..position-1] that are greater than key to
        #one position ahead of their current position.
        while position > 0 and arr[position-1] > key:
            arr[position] = arr[position-1]
            position = position - 1
            
        arr[position] = key
    return arr


# In[18]:


def recursive_insertion_sort(arr):
    if len(arr) == 1:
        return arr
    else:
        key = arr[0]
        position = 0
        
        while position > 0 and arr[postion-1] > key:
            arr[position] = arr[position-1]
            position -= 1
        
        arr[position] = key
        
        return [arr[0]] + recursive_insertion_sort(arr[1:])
    


# In[19]:


insertion_sort(test)


# In[20]:


recursive_insertion_sort(test)


# ## Merge sort
# 
# Worst-case time complexity: $O(n\log{n})$
# 
# ### Algorithm
# 
# 1.   Split the array into 2 sub-arrays recursively until sub-arrays contain only one single element.
# 2.   Merge the sub-arrays into a single array.
# > 1.    Compare the first $n$ elements of the sub-arrays.
#   2.    The smaller of the two elements is appended to the new array
#   3.    Repeat until both sub-arrays are empty.
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 

# In[11]:


def merge_sort(arr, l, r):
    if l < r:
        m = (l+r) // 2
        
        merge_sort(arr, l, m) #Sort first and second halves
        merge_sort(arr, m+1, r)
        
        return merge(arr, l, m, r)
      
def merge(arr, l, m, r):
    #copy data into temp arrays L and R
    L = arr[l:m+1]
    R = arr[m+1:r+1]
        
    #merge the temp arrays back into arr[l..r]
    i = 0
    j = 0
    k = l 
    
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    #Copy remaining elements in temp array back into original array
    while i < len(L): 
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1
    
    return arr


# In[12]:


merge_sort(test, 0, 9)


# ## Quicksort
# 
# Worst-case time complexity: $O(n^2)$
# 
# ### Notes
# 2 pointers (left pointer and right pointer) are maintained for insertion of pivot into the correct position. The pointers are moved towards each other. When left pointer element > pivot and right pointer element < pivot, the elements are swapped. When the pointers cross over, the final position of the pivot is given by the right pointer.
# 
# ### Algorithm
# 1. Assign the pivot to be the first element.
# 2. Partition the array using the pivot.
# 3. Recursively sort the array by partitioning until the sub-array contains only one single element.

# In[23]:


#Double pointer implementation
def quicksort(arr, first, last):
    if first < last:
        splitpoint = partition(arr, first, last)
        quicksort(arr, first, splitpoint-1)
        quicksort(arr, splitpoint+1, last)

    return arr

def partition(arr, first, last):
    pivot = arr[first]

    leftmark = first + 1
    rightmark = last 

    done = False

    while not done:
        while leftmark <= rightmark and arr[leftmark] <= pivot:
            leftmark += 1

        while rightmark >= leftmark and arr[rightmark] >= pivot:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            temp = arr[leftmark]
            arr[leftmark] = arr[rightmark]
            arr[rightmark] = temp

    temp = arr[first]
    arr[first] = arr[rightmark]
    arr[rightmark] = temp

    return rightmark


# In[24]:


quicksort(test, 0, len(test)-1)


# In[25]:


#Single pointer implementation
def quicksort(arr, first, last):
    if first < last:
        splitpoint = partition(arr, first, last)
        quicksort(arr, first, splitpoint-1)
        quicksort(arr, splitpoint+1, last)

    return arr

def partition(arr, first, last):
    pivot = arr[last]
    pointer = first
    
    for index in range(first, last):
        if arr[index] < pivot:
            temp = arr[pointer]
            arr[pointer] = arr[index]
            arr[index] = temp
            pointer += 1

        
    temp = arr[pointer]
    arr[pointer] = pivot
    arr[last] = temp

    return pointer


# In[26]:


quicksort(test, 0, len(test)-1)


# # Search Algorithms
# 
# Implement search algorithms.
# 
# *   Linear Search
# *   Binary Search
# *   Hash Table Search
# 
# 
# 
# 
# 

# ## Linear Search
# 
# Worst-case time complexity: $O(n)$

# In[48]:


def linear_search(item, arr):
    i = 0
    listsize = len(arr)

    while i < listsize:
        if arr[i] == item:
            return i
        i += 1
    
    return -1 #not found


# In[49]:


linear_search(test[0], test)


# In[50]:


linear_search(99999, test)


# ## Binary Search
# Worst-case time complexity: $O(\log{n})$
# 
# ### Notes
# Array has to be sorted first.

# In[28]:


def binary_search(item, arr):
    first = 0
    last = len(arr) - 1
    found = False

    while first <= last and not found:
        middle = (first+last)//2
        if arr[middle] == item:
            found = True
        else:
            if item < arr[middle]:
                last = middle - 1
            else:
                first = middle + 1

    return found 


# In[41]:


def recursive_binary_search(item, arr, first, last):
    if first > last:
        return False
    else:
        middle = (first+last)//2
        if arr[middle] == item:
            return True
        else:
            if item < arr[middle]:
                return recursive_binary_search(item, arr, first, middle-1)
            else:
                return recursive_binary_search(item, arr, middle+1, last)


# In[42]:


binary_search(test[0], test)


# In[43]:


binary_search(99999, test)


# In[44]:


recursive_binary_search(test[0], test, 0, len(test) - 1)


# In[45]:


recursive_binary_search(99999, test, 0, len(test) - 1)


# ## Hash Table Search
# 
# Worst-case time complexity: $O(1)$
# 
# ### Notes
# To create a hash: Use hash_total % array size
# 
# 
# 

# In[30]:


class MyHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.slots = [None] * self.capacity

    def hash_function(self, key):
        #Weighted ordinal hash
        key = str(key)
        i = 0
        hash = 0
        while i < len(key):
            hash += key[i] * i
            i += 1
        hash = hash % self.capacity
        return hash 

    def insert(self, key, data):
        position = self.hash_function(key)
        orig = position
        while True:
            if self.slots[position] is None: #Empty slot at hash value
                self.slots[position] = (key, data)
                return 0  
            elif self.slots[position][0] == key: #key already exists
                self.slots[position] = (key, data) #Update
                return 1
            
            position = (position + 1) % self.capacity
            if position == orig:
                return -1 #Hash table is full

    def search(self, search_key):
        position = self.hash_function(search_key)
        if self.slots[position] is None:
            return -1 #Record not in hash table
        for i in range(self.capacity):
            probe = (position + i) % self.capacity
            if self.slots[probe][0] == search_key:
                return self.slots[probe][1] #Record found
        return -1 #Record not in hash table


# In[ ]:




