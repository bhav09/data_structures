#it is to visualize algorithms

from algovis import sorting
import random
import time

the_list = [i for i in range(1,100)]
random.shuffle(the_list)
print(the_list)

b_start = time.time()
bubble = sorting.BubbleSort(the_list)
bubble.visualize(interval=10,reverse=True)
b_end = time.time()
print('Time taken for Bubble sort:',b_end-b_start)

i_start = time.time()
isort = sorting.InsertionSort(the_list)
isort.visualize(interval=10,reverse=True)
i_end = time.time()
print('Time taken for Insertion sort:',i_end-i_start)

m_start = time.time()
merge = sorting.MergeSort(the_list)
merge.visualize(interval=10,reverse=True)
m_end = time.time()
print('Time taken for Merge sort:',m_end-m_start)

q_start = time.time()
quick = sorting.QuickSort(the_list)
quick.visualize(interval=10,reverse=True)
q_end = time.time()
print('Time taken for Quick sort:',q_end-q_start)

#bubble.code()
