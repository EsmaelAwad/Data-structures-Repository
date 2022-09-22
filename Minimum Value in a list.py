"""
In this problem we want to determine the minimum number in a list.
Our variables:
    1-The list
Thinking through the problem:
    we might compare each element with all the elements of the list,
    and if the sum of the returned array is 0 this means that this is
    indeed, the smallest number! OOOPs that's only with numpy'
"""
a_list = [1,2,3,4,5,6]

#print((a_list[2] > 6)+0)


def minmax1 (x):
    # this function fails if the list length is 0 
    minimum = maximum = x[0]
    for i in x[1:]:
        
        if i < minimum: 
            minimum = i
            
        elif i > maximum:
            maximum = i
    return (minimum,maximum)

print(minmax1([9,8,7,6,5,4,3,2,1,11,12,13,14,15,16,17,18,19]))
print(minmax1([1,-10]))
print(minmax1([-20, 0, 2, 7, 5, -1, -2]))

def count_element( array , x ):
    i = 0
    if x in array :
        
        while i < len( array ) and array[i] != x :
            i += 1
        return i
    else:
        return "The element is not in the array"
print(count_element([1,"m","n","556",125],"n"))