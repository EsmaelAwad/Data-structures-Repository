'''
Thinking About the problem:
    
    We want to determine the index of an eleement in a list.
    [7,6,5,4,3,2,1], What is the index of 4 ?

Thinking About our Variables:
    1-The list
    2-The number to look for in the list
    3-The index of the number we are looking for in the list!

From point 3 :
    The index has to change it's Value so that it locates our query (2)

Test we want to look out for:
    1- The element is not in the list! ----priority : High
    2- The element is duplicated! --- Python's nature will return the first one it faces in the positive direction (specified Direction)
        we will define an algorithm that gets the shortest path later.
'''


def locate_number(numbers,query):
    
    if query not in numbers :
        return -1
    init_index = 0
    while True:
        output = numbers[init_index]
        if output == query :
            return init_index
        else:
            init_index += 1
            output = numbers[init_index]
            if output == query :
                return init_index

print(locate_number([x for x in range(10000)],1))

'''
We want to develop a function that sums all numbers that are less than or
equal to the provided number.
'''

def sum_to_num(n):
    my_sum = 0
    i=0
    #replace this pass (a do-nothing) statement with your code
    while i <= n:
        my_sum = my_sum + i
        #print(my_sum)
        i+=1
    return my_sum

def sum_to_num_fast(n):
    return n*(n+1)/2


#print(sum_to_num_fast(55555555555555555555555555000000000000000000000000000))
#print(sum_to_num(100000))

        