
#This script will reverse the words in the string. Basically here we will traverse the string and once we find the whitespace, 
#   that substring will be kept in reversed order in a new string. The process is continued till it reaches the end of string. 

s = "How are you Brother"

# Output: woH era uoy rehtorB

sub = ""
new = ""


l = len(s)
for i in s:
	if i!= " ":
		sub = sub + i
		l = l -1
		if l == 0:
			new = new +sub[::-1]
	else:
		#print i
		new = new + sub[::-1] + i
		sub = ""
		l = l-1
		#print l
print new 
