#finding the leftmost char that is repeated

def repeat(s):
	d={}
	idx=-1
	for i in range(len(s)):
		if s[i] not in d:
			d.update({s[i]:i})
		else:
			idx=d[s[i]]
			break
	return idx
s='abcd'
repeat(s)