from algovis import sorting
import random,time

the_list = [i for i in range(1,100)]
random.shuffle(the_list)
print(the_list)

s_start = time.time()
selection = sorting.SelectionSort(the_list)
selection.visualize(interval=10,reverse=True) #to visualize
s_end = time.time()
print('Time taken for Bubble sort:',b_end-b_start)

selection.info() #info about the algo
print()
print('-----------------------------------------------------------------------------------------------------------------')
print()
selection.code() #pseudo code behind the algoritm
