
# This script will spit out all the anagrams of string "p" which are present in the string "s".


s = "cbaezdpabcbabacdfzcab" 
p = "abc"
new = ""

for i in range(len(s)):
	if (i <= (len(s) - len(p))): #Making sure the slicing operator doesn't go below size of stirng "p"
		new = s[i:(i+3)]
		if ((''.join(sorted(p))) == (''.join(sorted(new)))): #Bascially comparing the sorted version of string "p" with the sliced "new" string
			print "Anagram:" + new + " is at index: " +str(i)
