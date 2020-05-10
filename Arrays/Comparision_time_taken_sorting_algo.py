import time

def selection_sort(sel_sort):  
# Traverse through all array elements 
    for i in range(len(sel_sort)): 
      
    # Find the minimum element in remaining unsorted array 
        min_idx = i 
        for j in range(i+1, len(sel_sort)): 
            if sel_sort[min_idx] > sel_sort[j]: 
                min_idx = j 
              
    # Swap the found minimum element with  
    # the first element         
        sel_sort[i], sel_sort[min_idx] = sel_sort[min_idx], sel_sort[i] 
    print('Selection Sort :',sel_sort)

def bubble_sort(b_sort):
    
    n=len(b_sort)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if b_sort[j]>b_sort[j+1]: #comparing and swapping every other element of the list
                b_sort[j+1],b_sort[j]=b_sort[j],b_sort[j+1]    
    print('Bubble Sort :',b_sort)

start_pgm=time.time()
A = [64, 42, 32, 22, 11]

sel_sort,b_sort,inbuilt=A,A,A
print('Unsorted:', A)

#selection sort----------
start_sel=time.time()
selection_sort(sel_sort)
end_sel=time.time()
sel_time=end_sel-start_sel
print('Time taken for Selection Sort:',sel_time)
print()

#inbuilt function--------
start_inbuilt=time.time()
b=inbuilt
b=sorted(b)
end_inbuilt=time.time()
inbuilt_time=end_inbuilt-start_inbuilt
#print(b)


#bubble sort-----------
start_bubble=time.time()
bubble_sort(b_sort)
end_bubble=time.time()
b_time=end_bubble-start_bubble
print('Time taken for Bubble Sort:',b_time)
print()

end_pgm=time.time()
tot_time=end_pgm-start_pgm


#print('Time taken for Python-s inbuilt sorting function:',inbuilt_time)

print('\nTime taken for the Entire program:',tot_time)




