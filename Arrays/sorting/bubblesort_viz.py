from algovis import sorting
import random,time

the_list = [i for i in range(1,100)]
random.shuffle(the_list)
print(the_list)

b_start = time.time()
bubble = sorting.BubbleSort(the_list)
bubble.visualize(interval=10,reverse=True) #to visualize
b_end = time.time()
print('Time taken for Bubble sort:',b_end-b_start)

bubble.info() #info about the algo
print()
print('-----------------------------------------------------------------------------------------------------------------')
print()
bubble.code() #pseudo code behind the algorithm
