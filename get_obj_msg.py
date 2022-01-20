##################################
# 获取对象信息
##################################

import class_instance


# 判断对象类型
import types

##################################
# type()
##################################

print(type(123))
print(type('123'))
print(type(None))

print(type(abs))

print(type(123) == int)

# 如果是基本类型 我们可以写 int str 但是如果是函数 我们可以使用types来进行判断
def fn():
    pass


print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)
##################################
# isinstance()对于class的继承关系来说使用type很不方便
##################################
class Animal(object):
    def run(self):
        print('animal is running')


class Dog(Animal):
    def run(self):
        print('dog is running')


class Cat(Animal):
    def run(self):
        print('cat is running')

a = Animal()
d = Dog()
c = Cat()

# 使用isinstance进行判断类
print(isinstance(a, Animal))
print(isinstance(d, Animal))

# 也可以判断基本类型
print(isinstance('a', str))
print(isinstance(123, int))
print(isinstance(b'a', bytes))

# 也可以判断变量是某些类型的一种
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))


##################################
# dir() 如果想获得一个对象的属性和方法可以使用该函数
##################################

print(dir('ABC'))

# 仅仅打印对象的属性和方法是不够的
class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

obj = MyObject()

print(hasattr(obj, 'x'))
print(hasattr(obj, 'y'))
print(setattr(obj, 'y', 19))
print(hasattr(obj, 'y'))

# 获取属性不存在也可以返回默认值
print(getattr(obj, 'z', 192))

# 也可以获得对象的方法
fn = getattr(obj, 'power')
print(fn)
print(fn())





