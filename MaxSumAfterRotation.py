
def getSum(a: int, n: int)->int:
    sum = 0
    i = 0
    while i < n:
        sum += a[i]
        i += 1
    return sum

def getOrderedSum(a: int, n: int)->int:
    sum = 0
    i = 0
    while i < n:
        sum += (a[i]*i)
        i += 1
    return sum

def max_sum(a, n):
    totalSum = getSum(a, n)
    S = maxSum = getOrderedSum(a, n)
    # print(maxSum, totalSum)
    
    i = 1
    while i < n:
        S = sum = (S - totalSum + (a[i-1]*n))
        if sum > maxSum:
            maxSum = sum
        i += 1
    
    return maxSum


n = 84
arr = [887, 778, 916, 794, 336, 387, 493, 650, 422, 363, 28, 691, 60, 764, 927, 541, 427, 173, 737, 212, 369, 568, 430, 783, 531, 863, 124, 68, 136, 930, 803, 23, 59, 70, 168, 394, 457, 12, 43, 230, 374, 422, 920, 785, 538, 199, 325, 316, 371, 414, 527, 92, 981, 957, 874, 863, 171, 997, 282, 306, 926, 85, 328, 337, 506, 847, 730, 314, 858, 125, 896, 583, 546, 815, 368, 435, 365, 44, 751, 88, 809, 277, 179, 789]

max_sum(arr, n)

# Its Correct output is:
# 1805686

# And Your Code's output is:
# 1660114