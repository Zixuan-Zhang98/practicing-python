x = 'outside'

def report():
    global x # this will get a reference to the global variable x
    x = 'inside'
    return x

print(report()) # inside
print(x)        # outside

# LEGB Rule:
#   Local
#   Enclosing
#   Global
#   Built in
def local():
    x = 'Local'
    return x

x = 'Global'

def enclosing():
    # x = 'Enclosing'
    def inside():
        print(x)
    inside()

enclosing()

print(max(2,3))

num = 1
def changeNum(num): # this function won't change the global num since int is immutable tyoe
    num = 2
print(num)
changeNum(num)
print(num)

