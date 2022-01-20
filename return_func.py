##################################
# 返回函数
##################################

# 函数返回结果为函数
def lazy_sum(*args):
    print('args参数', args)
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum


sum = lazy_sum(1,3,5,7)
# sum = lazy_sum(list(range(20)))
print(sum())

##################################
# 闭包
# 返回函数不要引用任何循环变量，或者后续会发生变化的变量。
##################################

def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1(), f2(), f3())

def count1():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs

f1, f2, f3 = count1()
print(f1(), f2(), f3())
