def mi_dec(f):
    def interno(*args, **kwargs):
        print("Los argumentos son: {0} {1}\n".format(*args,**kwargs))
        return f(*args,**kwargs)
    return interno

@mi_dec
def f_1(x, y=1):
    return (x + 1) ** y

def f_2(x, y):
    return x * y

print(f_1(1,2))
print(f_2(2,2))
