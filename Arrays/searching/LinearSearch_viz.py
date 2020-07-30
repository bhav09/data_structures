from algovis import searching
import random

the_list = [i for i in range(100)]
random.shuffle(the_list)
print(the_list)

l_search = searching.LinearSearch(the_list)
l_search.search(51,steps=True)
l_search.visualize(51,interval=100)

print()
print('-----------------------------------------------------------------------------------------------------------------')
print()
l_search.info()

print()
print('-----------------------------------------------------------------------------------------------------------------')
print()
l_search.code()
