import time


def decorator_function(func):
    def wrapper_function():
        time.sleep(3)
        func()
        time.sleep(1)
        func()
    return wrapper_function


@decorator_function
def say_hello():
    print("Hello, world!")


def say_goodbye():
    print("Goodbye, world!")


def say_greeting():
    print("How are you?")


say_hello()