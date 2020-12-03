#!python
from recursive_sorting import merge_sort

def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum integer values)
    # TODO: Create list of counts with a slot for each number in input range
    # TODO: Loop over given numbers and increment each number's count
    # TODO: Loop over counts and append that many numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list
    if len(numbers) < 2:
        return 
    min_value = min(numbers)
    max_value = max(numbers)

    range_number = max_value - min_value + 1 

    array = [0] * range_number

    for number in numbers:
        array[number - min_value] += 1 
    i, j= 0,0
    while i < len(numbers):
        while array[j] < 1:
            j += 1
        number[i] = min_value + j
        array[j] -= 1
        i += 1 

def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list
    if len(numbers) < 2:
        return 
    max_value = max(numbers)
    min_value = min(numbers)
    bucket_range = (max_value - min_value) // num_buckets + 1

    buckets = [[] for _ in range(num_buckets)]
    
    for item in numbers:
        index = (item - min_value) // bucket_range
        buckets[index].append(item)

    for i in range(len(buckets)):
        merge_sort(buckets[i])
    
    i = 0 
    for bucket in buckets: 
        for item in bucket:
            numbers[i] = item
            i += 1 

