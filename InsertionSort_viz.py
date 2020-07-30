from algovis import sorting
import random,time

the_list = [i for i in range(1,100)]
random.shuffle(the_list)
print(the_list)

i_start = time.time()
isort = sorting.InsertionSort(the_list)
isort.visualize(interval=10,reverse=True) #to visualize
i_end = time.time()
print('Time taken for Bubble sort:',b_end-b_start)

isort.info() #info about the algo
print()
print('-----------------------------------------------------------------------------------------------------------------')
print()
isort.code() #pseudo code behind the algorithm
