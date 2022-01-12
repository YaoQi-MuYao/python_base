from collections.abc import Iterable

##################################
# 迭代
##################################

##################################
# dict 的迭代方式
##################################
d = {'a': '1', 'b': '2'}

# 默认迭代dict的key
for k in d:
    print(k)

# 如果想迭代value可以这样
for v in d.values():
    print(v)

# 也可以同时迭代key和value
for k, v in d.items():
    print('key', k, 'value', v)


##################################
# str迭代
##################################

s = 'muyao'
for s1 in s:
    print(s1)

# 判断一个对象是否可迭代
print(isinstance('abc', Iterable))

# 如果想对可迭代对象迭代 同时显示下标 那么可以使用函数enumerate
L = list(range(20))
for i, value in enumerate('abc'):
    print(i, value)