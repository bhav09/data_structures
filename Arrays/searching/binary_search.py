my_list=[]
#enter 10 elements
for i in range(10):
    val=int(input('Enter Element'))
    my_list.append(val)
x=int(input('Enter the element to be searched:'))
flag=0
beg=0
end=len(my_list)-1

while beg<=end:
    mid=(beg+end)//2
    if x<my_list[mid]:
        end=mid-1
    elif x>my_list[mid]:
        beg=mid+1
    elif x==my_list[mid]:
        flag=1
        break
    else:
        #print('Not Found')
        break
if flag==0:
    print('Element Not Found')
else:
    print('Element Found')
