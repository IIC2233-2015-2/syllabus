def mi_dec(f):
    def interno(*args, **kwargs):
        print("Los argumentos son: {0} {1}\n".format(*args,**kwargs))
        return f(*args,**kwargs)
    return interno

def f_1(y, x=1):
    return x - y

@mi_dec
def f_2(x, y):
    return (x + 1) * y

print(f_1(6,7))
print(f_2(2,2))
