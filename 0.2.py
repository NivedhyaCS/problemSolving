def decorator(func):
    def wrapper():
        print('perform berfore fn call')
        func()
        print('perform after fn call')
    return wrapper

@decorator
def say_hello():
    print("hello")
say_hello()