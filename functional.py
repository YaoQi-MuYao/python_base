from functools import reduce

##################################
# 函数式编程
##################################

##################################
# 高阶函数
##################################

# 将函数已参数的形式传入别的函数

f = abs


def add(x, y, f):
    return f(x) + f(y)


print(add(5, -6, f))


##################################
# map()/reduce()
##################################


# map() 函数接受两个参数，一个是函数，一个是Iterable,
# map() 将传入的函数一次作用在序列的每个元素，并返回Iterator结果
def f(x):
    return x * x


r = map(f, range(10))
print(list(r))

r = map(str, range(10))
print(list(r))


# reduce() 接受一个函数和一个序列 函数必须接受两个参数
# reduce() 把函数结果和序列的下一个元素做累计计算
def add(x, y):
    return x + y


print(reduce(add, range(8)))

def fn(x, y):
    return x * 10 + y


print(reduce(fn, range(8)))

# 将序列 s 首字母大写 其他字母小写
s = ['adam', 'LISA', 'barT']

def normalize(name):
    names = [str.upper(v) if i == 0 else str.lower(v) for i, v in enumerate(name)]
    return "".join(names)


print(list(map(normalize, s)))

# 使用reduce() 接受一个list 并求积
def prod(L):
    def mu(x, y):
        return x * y
    return reduce(mu, L)


print(prod([3, 5, 7, 9]))

##################################
# filter() 函数
##################################

#filter()函数 与map()函数类似 接受一个函数和一个序列 返回Iterator

def is_odd(n):
    return n % 2 == 1


print(list(filter(is_odd, range(20))))

##################################
# sorted()函数 第一个参数是序列 第二个关键字参数是 限制条件函数
# 第三个关键字参数是 是否反向排序
##################################

# sorted()函数可以排序list 也是高阶函数可以传函数参数作为条件
L = [36, 5, -12, 9, -21]
print(sorted(L))
print(sorted(L, key=abs))

L = ['bob', 'about', 'Zoo', 'Credit']
print(sorted(L))
print(sorted(L, key=str.lower, reverse=True))


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0].lower()


print(sorted(L, key=by_name))

def by_score(t):
    return t[1]


print(sorted(L, key=by_score, reverse=True))