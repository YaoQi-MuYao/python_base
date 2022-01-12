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