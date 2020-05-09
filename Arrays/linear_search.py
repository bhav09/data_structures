my_list=[]
f=0
index=[]

print('Enter 5 Elements to the list')
for j in range(5):
    val=int(input())
    my_list.append(val)
print('Your List is :',my_list)  #printing the list

x=int(input('Element to be searched:'))
print('Entered Element is : ',x)

for i in range(5):   #searching the element 
    if my_list[i]==x:
        f=1
        index.append(i) 

if f==1:
    print('Element found at :',index)
else:
    print('Not Found')
