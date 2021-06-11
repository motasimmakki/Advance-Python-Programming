
def isValidPair(num1: int, num2: int)->bool:
    if((num1 > 0) and (num2 <= 0)):
        return  True
    if((num1 <= 0) and (num2 > 0)):
        return  True
    return False

def getPairs(A: list, n :int)->int:
    mapedIndex = {}
    
    i = 1
    while(i < n):
        if(isValidPair(A[i-1], A[i])):
            mapedIndex[i-1] = abs((abs(A[i-1]) - abs(A[i])))
        i += 1

    # print(mapedIndex)
    mapedIndex = dict(sorted(mapedIndex.items(), key=lambda item: item[1]))
    # print(mapedIndex)
    
    pairs = []
    for key in mapedIndex:
        if((A[key] != None) and (A[key+1] != None)):
            pairs.append(A[key])
            pairs.append(A[key+1])
            A[key] = None
            A[key+1] = None

    # print(pairs)
    return pairs

A = [1, 2, -3, 4]
# A = [1, -3, 2, -3, 4]
size = len(A)

print("Array: ", A)
print("Result: ", getPairs(A, size))
# getPairs(A, size)
