from typing import Callable
# print(5)
# print(print)
#
# new_print = print
# print(new_print is print)

def my_function(number):
    result = number * 22
    return result

def my_scrudge_function(func: Callable, *args, **kwargs):
    print(func)
    print(func(*args, **kwargs))
    result = func(*args, **kwargs)
    return result



print(my_function)

res = my_scrudge_function(my_function, 5)
print(res)
