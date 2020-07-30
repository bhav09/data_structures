from algovis import sorting
import random,time

the_list = [i for i in range(1,100)]
random.shuffle(the_list)
print(the_list)

m_start = time.time()
merge = sorting.SelectionSort(the_list)
merge.visualize(interval=10,reverse=True) #to visualize
m_end = time.time()
print('Time taken for Bubble sort:',m_end-m_start)

merge.info() #info about the algo
print()
print('-----------------------------------------------------------------------------------------------------------------')
print()
merge.code() #pseudo code behind the algoritm
