# Anjali and Vaibhavi are playing a game with a pile of N coins.
# In this game, Anjali and Vaibhavi make their respective moves alternately, starting with Anjali.

# In a turn, a player can remove x coins from the pile if x satisfies :
# 1<= x <= n
# x & n = 0 (bitwise and of x and n is 0.)

# where 'n' is the size of the pile in the current turn.
# The player who is unable to make a move loses the game.
# Given the initial number of coins in a pile, determine who would win the game.
# Assume that both the players play optimally throughout the game.

# Input Format:
# First line denotes t  i.e. number of test cases
# Next ‘t’ lines contain n where n is the number of coins in the pile as the game commences.

# Output Format:
# For each test case, print the winning player’s name (case sensitive).

def allSet(num: int)->bool:
    
    myNum = num
    count = 0
    while num:
        num >>= 1
        count +=1
    
    if myNum == (2**count)-1:
    	return True
    return False
    
def getPilesResult(coins: int)->str:
     
    if allSet(coins) | (coins == 1):
        return "Vaibhavi"    
	
    # 0 for Anjali, and 1 for Vaibhavi.
    chance = 0

    while not allSet(coins):        
        x = 1
        while (x & coins) != 0:
            x <<= 1
        if x >= coins:
            break
        
        coins -=x

        if chance:
            chance = 0
        else:
            chance = 1

    if chance:
        winner = "Anjali"
    else:
        winner = "Vaibhavi"

    return winner

t = int(input())
coins = [None]*t

for i in range(0, t):
    coins[i] = int(input())

for i in range(0, t):
    print(getPilesResult(coins[i]))


# Test Case : 1
# 5
# 1
# 2
# 3 
# 4
# 5

# Output :
# Vaibhavi
# Anjali
# Vaibhavi
# Anjali
# Anjali

# Test Case : 2
# 5
# 10
# 12 
# 15
# 22
# 25

# Output :
# Anjali
# Vaibhavi
# Vaibhavi
# Anjali
# Vaibhavi

# Test Case : 3
# 7
# 4
# 6
# 8
# 10
# 12
# 45
# 48

# Output :
# Anjali
# Vaibhavi
# Anjali
# Anjali
# Vaibhavi
# Anjali
# Vaibhavi

 	   