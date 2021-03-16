x = 'global x'

def outer():
    def inner():
        print(x)
    
    inner()
    print(x)

outer()
print(x)