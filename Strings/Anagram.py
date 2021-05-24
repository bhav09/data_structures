#to find whether two string are anagrams or not

def anagram(s1,s2):
	d1,d2={},{}
	flag=0
	for i in s1:
		if i not in d1:
			d1[i]=1
		else:
			d1[i]+=1
	for j in s2:
		if j not in d2:
			d2[j]=1
		else:
			d2[j]+=1
	if len(d1)==len(d2):
		for i in d1:
			if d1[i]==d2[i]:
				flag=1
			else:
				flag=0
	if flag==0:
		return 'Not Anagram'
	else:
		return 'Anagram'

anagram('abcd','cdba')