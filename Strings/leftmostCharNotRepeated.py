#finding the lefmost element that doens't repeat
def notrepeat(s):
	occ=[0]*255
	length=len(s)
	val=-len(s)+1
	for i in range(length):
		if occ[ord(s[i])]==0:
			occ[ord(s[i])]=val
			val+=1
		else:
			occ[ord(s[i])]=10
	minn=min(occ)
	idx=chr(occ.index(minn))
	return s.index(idx)

s='abbacceda'
notrepeat(s)