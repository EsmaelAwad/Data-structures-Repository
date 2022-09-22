import timeit
from timeit import Timer
#Most basic way is.
#print([] + [1,2,3,4])

# 1

def add_by_concat():
    l = []
    for i in range(1000):
        l += [i]
    return l

# 2

def add_by_appending():
    l = []
    for i in range(1000):
        l.append(i)
    return l

# 3

def add_by_list_comprehension():
    l = [x for x in range(1000)]
    return l

# 4 
def add_by_range():
    l = list(range(1000))
    return l


t1 = Timer("add_by_concat()","from __main__ import add_by_concat")
print("Concat",t1.timeit(1000)," Milleseconds\n")
t2 = Timer("add_by_appending()","from __main__ import add_by_appending")
print("Append",t1.timeit(1000)," Milleseconds\n")
t3 = Timer("add_by_list_comprehension()","from __main__ import add_by_list_comprehension")
print("List Comprehension",t1.timeit(1000)," Milleseconds\n")
t4 = Timer("add_by_range()","from __main__ import add_by_range")
print("Range",t1.timeit(1000)," Milleseconds\n")

