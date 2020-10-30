
def is_sorted(items):
    #TODO: return a bool indicating whether the items are sorted or not
    for i in range(len(items)-1):
        if items[i] >= items[i + 1]: 
            return False
    return True

#compare each item in the list to the one after it 
#-1 to stop at end of list and it doesnt go over 
        
print(is_sorted([1,3,5,10,20]))#expecting True
print(is_sorted([20,3,5,10,1]))#expecting False

