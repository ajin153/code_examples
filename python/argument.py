"""使用*和**传递可变参数"""
def tracer(func,  *pargs, **kargs):
    print("Calling:", func.__name__)
    return func(*pargs, **kargs)

def func(a, b, c, d): return a + b + c + d

print(tracer(func, 1, 2, c=3, d=4))
# 注：python 2版本中可以考虑使用apply()来使用可变参数