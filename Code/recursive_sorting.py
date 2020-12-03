#!python

def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until one list is empty
    # TODO: Find minimum item in both lists and append it to new list
    # TODO: Append remaining items in non-empty list to new list
    new_arr = []
    i = 0 
    j = 0
    while i < len(items1) and j < len(items2): # while the index in array one is less than the length of array 1 ~ only if its in range do we go through loop
        if items1[i] <= items2[j]: # if the index in array one is less than the index in array 2
            new_arr.append(items1[i]) # then we append the elemnent in items1 to the new array
            i += 1 # we move the pointer to the next number to the right
        if items2[j] < items1[i]: # if the element in second is less than the element in first 
            new_arr.append(items2[j]) #add it to the new array 
            j += 1
    return new_arr #return new sorted array

def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order
    #a sub: 2,4,7,8
    #b sub: 1,3,11
    #sorted: empty
    #we look at first element on both subs - the smallest one goes into sorted array
    #sorted:1 
    #then we take a look at the second element on second sub and compare to the first element on the first one 
    # b 3 is > a 2 so we add 2 to sorted array
    #sorted: 1, 2, 
    #using same logic, we move through the rest and end up with sorted: 1, 2, 3, 4, 7, 8, 11

    if len(items) <= 1: #if the list is one - (and/or is at the last element) ~  then it is sorted
        return items #return the list of the items 
    
    mid_point = len(items)//2 #split the list into two 
    items1 = merge_sort(items[:mid_point]) #first half of list is everything before midpoint 
    items2 = merge_sort(items[mid_point:]) #second half is everything at midpoint and everything after it

    sorted_items = merge(items1, items2, items) #items are merged with helper function 
    items[:] = sorted_items #all the itemsm from both lists are sorted

    return items #return sorted list 

def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p

    divider = low 
    pivot = high 

    for i in range(low, high): #loop through all items in range of low to high 
        if items[i] < items[pivot]: #if the current item is less than the pivot 
            items[i], items[divider] = items[divider], items[i] #swap them items so that the lower num is to the left
            divider += 1
    items[pivot], items[divider] = items[divider], items[pivot] 
    return divider

def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort
    if low == None and high == None: #high and low ranges
        low = 0
        high = len(items)-1
    if low >= high: #already sorted so we return and break out 
        return
    p = partition(items, low, high) #partition items in-place around a pivot
    quick_sort(items, low, p-1) #sorting each sublist range by recursively calling quick sort
    quick_sort(items, p+1, high)

    return items