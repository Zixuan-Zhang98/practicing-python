def hello(name = 'Zixuan'):
    print('This is inside hello()')

    def greet():
        return '    This is inside greet()'

    def welcome():
        return '    This is inside welcome()'

    if name == 'Zixuan':
        return greet
    else:
        return welcome

x = hello(name='Stephany')
print(x())

def bye():
    return 'Bye Zixuan'

def other(func):
    print('Some other code')
    # Assume that func passed in is a function!
    print(func())

other(bye)

print('-------------------decorator------------------')

def new_decorator(func):

    def wrap_func():
        print('some code before executing func')

        func()

        print('some code after executing func')

    return wrap_func

@new_decorator
def func_needs_decorator():
    print('Please decorate me')

func_needs_decorator()

# func_needs_decorator = new_decorator(func_needs_decorator)
# func_needs_decorator()