#printing all permutations of a string
	
def permute(ch,curr_index=0):
	if curr_index==len(s)-1:
		print(''.join(ch))
	for i in range(curr_index,len(ch)):
		ch[i],ch[curr_index]=ch[curr_index],ch[i]
		permute(ch,curr_index+1)
		ch[i],ch[curr_index]=ch[curr_index],ch[i]
		
s='ABC'
permute(list(s))