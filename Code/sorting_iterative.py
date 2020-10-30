#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check that all adjacent items are in order, return early if so [ascending /descending order]
    for i in range(len(items)-1): #for every element in the list ~ We want to compare every element to the one that is right after it, which is why we add the -1 ~ it stops at the prev one and compares it to the last item 
        if items[i] >= items[i + 1]: #if element in list is more than or equal to the element that is immediately adjacent to it 
            return False #return false bc its not sorted ~ the items are not in order
    return True #We never hit a case after going through the whole loop where it is not sorted meaning it is sorted so we return True

    # for i in range(len(items)-1): #for loop - we have a definite end of the list that we want to check
    #     current = items[i] #set index(the position) ~ we use position to check the current element that we are looking at and the one next to it
    #     next_item = items[i + 1] #item next to current is position + 1 
    #     #assuming to check for ascending order
    #     if next_item <= current:
    #         return False # list is not sorted 
    # return True #if we checked all elements and there were no problems 

def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order
    #higher values to the right, lower values to the left
    sorted = False  #creating a local variable to break us out of loop whenever list has been sorted
    while not sorted: #we need to iterate through the list so we create a while loop- while the sorted = False variable is true, we go through this loop
        sorted = True #referencing local variable again 
        for i in range(0,len(items)-1): #-1 because we can't make a comparison on the last element on the list since there is not a num after it, so we'll do this until the -1 element
            if items[i] > items[i + 1]: #creating a comparison - if the i position(left) is greater than the i position(right, defined by i + 1)
                sorted = False # it is not sorted 
                items[i], items[i+1] = items[i+1], items[i] #we flip the two items on the list
    #whenever we have sorted all items the if statement won't activate and the sorted variable will remain True - it breaks us out of the while loop 
    return items #return sorted list

def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items