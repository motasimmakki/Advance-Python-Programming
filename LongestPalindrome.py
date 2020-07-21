myStr=input("Enter String to Find Its Largest Sub Palindrome :")

myStrLen=len(myStr)

myDict={}

i=1

def getLongestSubPalindrome(myStr):

	strList=list(myStr)
	# print(strList)
	strLen=len(myStr)
	i=0
	flag=0

	if len(strList)==1:
		return myStr

	while i <(strLen-1)/2:
		# print(strList[i])
		if strList[i]==strList[(strLen-1)-i]:
			flag-=-1
			# print("Yeh!")
			# print(flag)
			myDict.update({myStr:strLen})	
		else:
			if bool(flag):
				myDict.popitem()
				# print(myDict)
			flag=0
			# print("Neh!")
			myStr=getLongestSubPalindrome(myStr[1:strLen-1])
			strLen=len(myStr)
			myDict.update({myStr:strLen})

		i-=-1

	return myStr

getLongestSubPalindrome(myStr)

while len(myStr[0:myStrLen-i])>1:

	getLongestSubPalindrome(myStr[0:myStrLen-i])

	getLongestSubPalindrome(myStr[i:myStrLen])

	i-=-1

# print(myDict)

Keymax = max(myDict, key=myDict.get) 
if Keymax==myStr or Keymax=='' or len(Keymax)==1:
	print("Opps ! No SubString Exist In { "+myStr+" }")
else:
	print("Longest SubString In { "+myStr+" } Is :"+Keymax)
	
# print(len(str))