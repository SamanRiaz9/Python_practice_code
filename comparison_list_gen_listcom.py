import sys
import timeit
#make a generator
def gen():
    for item in range(100000):
        if item%2==0 and item%4==0 and item%8==0:
            yield item*item
print("size of gen is : ",sys.getsizeof(gen()),timeit.timeit())
#make list comprehension
x=[x*x for x in range(100000)if x%2==0 and x%4==0 and x%8==0]
print("size of list comprehension is : ",sys.getsizeof(x),timeit.timeit())
#make list
def list_check():
    k=[]
    for item in range(100000):
        if item%2==0 and item%4==0 and item%8==0:
            k.append(item*item)
print("size of list  is : ",sys.getsizeof(list_check()),timeit.timeit())

        





#     num = 0
#     while True:
#         yield num
#         num += 1
# print(next(gen()))


