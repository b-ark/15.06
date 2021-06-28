# Write a Python program to access a function inside a function (Tips: use function, which returns another function)
def first_foo():

    def second_foo():
        return 'second'

    return second_foo()


print(first_foo())
