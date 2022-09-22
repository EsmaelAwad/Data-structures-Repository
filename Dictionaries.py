my_dict = {"x":500,
           "y":400,
           "n":760}
print(my_dict["x"])
print("x" in my_dict)
del my_dict['x']
print(my_dict)
print(my_dict['y'] == 400)
my_dict['y'] = my_dict['y'] + 400
print(my_dict)
j = ["a","b","c","d","e"]
i = [1,2,3,4,5]
dict_comp = {j:i for (j,i) in zip(j,i)}
print(dict_comp)
dict_comp_ifs = {x:x**2 if x**2 % 2 == 0 else "Odd Number" for x in range(10)}
print(dict_comp_ifs)