def bubble_sort(items):
  #TODO: write code to implement the bubble sort algorithm
for i in range(len(items)): #controls the num passes - how many times we go through the list
    for j in range(len(items) - 1):
        if items[j] > items [j + 1]: #if the current is more than the next one, swap
            temp = items[j]
            items[j] = items[j+1]
            items[j+1] = temp

items = [3,1,7,0]
bubble_sort(items)
print(items) #should print [0, 1, 3, 7]

# items[j], items[j+1] = items[j+1], items[j]