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
# [1, 2, 3]
# n*n
# for i in range(len(arr)):
#    for j in range(len(arr)):
        # processing 
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
        sorted = True #referencing local variable again ~ to exit early to reduce the time complexity
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
    for i in range(len(items)): # for every element in in the list 
        min_value_index = i #we set a min value to the i position - we want the default to be the minimum value in the list 

        for j in range(i+1, len(items)): #for every element in the range of i + 1 (to the right) of the length of the list 
            if items[j] < items[min_value_index]: #if the value of j position in the list is less than the value of the position of the min value 
                min_value_index = j #replace the min vale to the value of the j position ~ we swap them

        if min_value_index != i: #if the min value no longer equals i (default)
            #if we find a value that has a lower value of than the default then we switch those items
            items[min_value_index], items[i] = items[i], items[min_value_index]

    return items # we return the list 

def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
    for i in range(1, len(items)): #the first item in the list is in the sorted list because there is no item to the left of it ~ we ignore the first one and look at all the values after it
        value_to_sort = items[i] #variable to sort the list ~ we store the i of element on the list 

        while items[i-1] > value_to_sort and i > 0: #while the item to the immediate left is greater than the value to sort (the item to the left is larger than the item to the right) i>0 because python allows neg indexing
            items[i], items[i-1] = items[i-1], items[i] #we swap the values 
            i = i -1 #we continue the comparisons down the list - incrementing the stepping down the list by comparing the element to the one to it's immediate left 
    return items #return the list 


if __name__ == "__main__":
    # print(is_sorted([1,2,3,4]))
    # print(bubble_sort([3,1,6,2]))
    # print(selection_sort([2,3,6,1]))
    print(insertion_sort([34,2,1,10,8,4,1]))