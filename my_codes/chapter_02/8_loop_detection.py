


def my_decorator(func):

    def wrapper():
        print("I am doing some boring work before executing func()")

        func()

        print("I am doing some boring work after executing func()")

    return wrapper


def my_function():
    print("I am the the original function")


@my_decorator
def my_function():
    print("I am the the original function")



my_function()



