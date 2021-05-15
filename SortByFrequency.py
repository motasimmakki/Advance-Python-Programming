import collections

# Input:
# 20
# 6 6 2 3 1 4 1 5 6 2 8 7 4 2 1 3 4 5 9 6
# Output:
# 6 6 6 6 1 1 1 2 2 2 4 4 4 3 3 5 5 7 8 9
   
#Function to sort the array according to frequency of elements.
def sortByFreq(a, n):
    
    frequency = {}
    arrangedList = [None]*n
    
    i = 0
    while i < n:
        if not (a[i] in frequency):
            frequency[a[i]] = 1
        else:
            frequency[a[i]] += 1
        i += 1
            
    # print(frequency)
    
    frequency = collections.OrderedDict(sorted(frequency.items()))
    data = sorted(frequency, key = frequency.get, reverse = True)
    # print(data)
    
    i = 0
    j = 0
    while i < len(data):
        while frequency[data[i]] != 0:
            arrangedList[j] = data[i]
            frequency[data[i]] -= 1
            j += 1
        i += 1
    
    return arrangedList

n = 20
arr = [6, 6, 2, 3, 1, 4, 1, 5, 6, 2, 8, 7, 4, 2, 1, 3, 4, 5, 9, 6]

print(sortByFreq(arr, n))