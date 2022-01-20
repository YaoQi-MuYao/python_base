##################################
# 偏函数
##################################


##################################
# 偏函数就是帮我们创建自定义函数
##################################
import functools

print(int('12345', base=8))

int2 = functools.partial(int, base=2)
print(int2('10000000'))

# 偏函数简单总结就是 简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单
int2 = functools.partial(int, base=2)
print(int2('10000000'))

# 上面的函数是固定了base参数为2 但其实也可以传入其他值
print(int2('100000000', base=10))

##################################
# 最后创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数
##################################

int2 = functools.partial(int, base=2)

# 相当于固定了int()函数的关键字参数base
print(int2('10010'))

# 相当于
kw = {'base': 2}
print(int('10010', **kw))

max2 = functools.partial(max, 10)
# 实际上会把10作为*agrs的一部分自动添加到左边
max2(5, 6, 7)

#相当于
agrs = (10, 5, 6, 7)
print(max(*agrs))