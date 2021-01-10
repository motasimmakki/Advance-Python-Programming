class Solution:
    def UniquesCharactersInAString(self, s: str) -> int:
    	
    	if len(s) == 0:
    		return 0
    	elif len(s) == 1:
    		return 1

    	s = sorted(s)

    	length = 0
    	itr = 0

    	while itr < len(s):
    		
    		if itr > 0:
    			while (s[itr] == s[itr-1]) and (itr+1 < len(s)):
    				itr += 1
    		
    		length += 1
    		itr += 1

    	return length-1
        
obj = Solution()

myStr = "abcabcbb"
# myStr = "bbbbb"
# myStr = "pwwkew"
# myStr = "A"
# myStr = ""

print("\nNumber of Unique Characters in a String are :", obj.UniquesCharactersInAString(myStr))