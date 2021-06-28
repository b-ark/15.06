# Write a Python program to detect the number of local variables declared in a function.
def foo1():
    a = 1
    b = 2
    c = []


def foo2():
    a = 1


def foo3():
    pass


def number_of_local_variables(function):
    return function.__code__.co_nlocals


def print_the_number(function):
    print(f'Number of local variables in function {function.__name__} = {number_of_local_variables(function)}')


print_the_number(foo1)
print_the_number(foo2)
print_the_number(foo3)
