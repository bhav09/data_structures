arr=[4,2,1,7,9,12]

lar,sec_lar=arr[0],arr[0]
for i in range(1,len(arr)):
	if arr[i]>lar:
		sec_lar=lar
		lar=arr[i]
	elif arr[i]<lar and arr[i]>sec_lar:
		sec_lar=arr[i]
print(sec_lar)