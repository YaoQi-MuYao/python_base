import os

##################################
# 列表生成式
##################################

# 列表生成式可以生成一些稍微复杂的list
L = [x * x for x in range(1, 11)]
print(L)

# 同时也可以在for后面加上if 过滤条件
# ps 这里的if是过滤 不是普通的if判断 所以不是表达式 不可以加else
var = [x * x for x in range(1, 11) if x % 2 == 0]
print(var)

# 当然也可以循环嵌套 不建议嵌套太多层
var = [m + n for m in 'ABC' for n in 'XYZ']
print(var)

# 获取当前路径的文件名称
var = [d for d in os.listdir()]
print(var)

##################################
# 生成器
# 根据数据循环生成list，节省内存
# 生成器返回的是generator 需要调用next() 获取下一个值
# 但generator是可以迭代的 所以可以迭代输出元素
##################################

var = (x * x for x in range(10))
for x in var:
    print(x)

# 斐波拉契算法

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a+b
        n = n + 1
        return 'done'


fib(6)