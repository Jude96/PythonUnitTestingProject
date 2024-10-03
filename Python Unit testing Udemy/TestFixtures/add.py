def example_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Calling the function with different keyword arguments
example_kwargs(name="John", age=30, city="Nairobi")
example_kwargs(brand="Toyota", model="Corolla", year=2022)


def example_args_kwargs(*args, **kwargs):
    print("Positional arguments:")
    for i, arg in enumerate(args):
        print(f"Argument {i}: {arg}")

    print("\nKeyword arguments:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# Calling the function with a mix of positional and keyword arguments
example_args_kwargs(1, 2, 3, name="Alice", age=25, city="Kisumu")


def example_args(*args):
    for i, arg in enumerate(args):
        print(f"Argument {i}: {arg}")

# Calling the function with different numbers of arguments
#example_args(1, 2, 3)
#example_args("apple", "banana", "cherry")


def add(*args):
    d = 0
    for i in args:
        d = d + i
    print(d)
    print(type(d))


#add(7,3,2,1,6,7,3,4,2,11,56777,21,3,5.09877,43,222)

def div(*args):
    try:
        f = args[0] / args[1]
        print(f)
    except ZeroDivisionError:
        print('Number canot be divided by zero')
    except TypeError:
        print('Wrong input types, try again')



div(0,"Apples",4)
