##################################
# python
# 函数的相关知识
##################################

##################################
# 参数相关
# 一共5种参数 可以随意组合使用
# 但是使用顺序必须遵循: 必选参数、默认参数、可变参数、命名关键字参数和关键字参数
# 最后对于任意函数 都可以使用类似 func(*args, **kw)的形式去调用
##################################

# 位置参数
def power(x):
    return x * x

##################################
# 默认参数
##################################
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


##################################
# 多个默认参数，调用顺序问题
# ps: 默认参数不可传入可变对象
##################################
def enroll(name, gender, age=6, city='ChengDu'):
    print('name', name)
    print('gender', gender)
    print('age', age)
    print('city', city)


# 按顺序调用默认参数
enroll('muyao', '男', 24)

# 不按顺序调用默认参数
enroll('muyao', '男', city='HaErBin')

##################################
# 可变参数 传入任意多个lit参数
# 在函数内部会转换为tuple
##################################
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


# 调用可变参数形式
# 可以简写
print(calc(1, 2, 3))

# 如果我们有已经定义好的的list或tuple可以直接传入
numbers = [1, 2, 3]
print(calc(numbers[0], numbers[1], numbers[2]))

# 或者简写形式
print(calc(*numbers))

##################################
# 关键字参数 可以传入任意多个含函数名的参数
# 函数内部自动封装为dict
# 可以直接传入必选参数
##################################
def person(name, age, **kw):
    print('name', name, 'age', age, 'other', kw)


# 可以只传入必传参数
person('muyao', 24)

# 也可以传入任意多个关键字参数
person('muyao', 24, gender='男', city='ChengDu')

# 如果我们有一个事先写好的dict可以直接传入
# 这里person 函数获取的是extra的一份拷贝
# 函数内部的操作不会影响extra的原数据
extra = {'gender': '男', 'city': 'ChengDu'}
person('muyao', 24, **extra)

##################################
# 命名关键字参数 可以限制关键字参数的传入
# 如果未传入必传的关键字参数则会抛异常
##################################

# 使用`*`分割 `*`后面的参数即为命名关键参数
def person1(name, age, *, city, job):
    print(name, age, city, job)


# 正常调用含有关键字参数函数
person1('muyao', 24, city='ChengDu', job='Java')

# 如果函数定义中有一个可变参数后面的命名关键字参数就不需要`*`做分割
def person2(name, age, *args, city, job):
    print(name, age, args, city, job)

# 命名关键字也可以设置缺省值
def person3(name, age, *, city='ChengDu', job):
    print(name, age, city, job)


# 调用含缺省值命名关键字函数时
person3('muyao', 24, job='Java')
