##################################
# 元类
##################################

from hello import Hello
h = Hello()
h.hello()

##################################
# type() 函数可以查看一个类型或变量的类型，Hello是一个class，
# 它的类型就是type，而h是一个实例，它的类型就是class Hello。
##################################

print(type(Hello))
print(type(h))

##################################
# type()函数既可以返回一个对象的类型，又可以创建出新的类型，
# 比如，我们可以通过type()函数创建出Hello类，
# 而无需通过class Hello(object)...的定义
##################################

def fn(self, name='world'):
    print('Hello, %s' % name)

Hello = type('Hello', (object,), dict(hello=fn))
h = Hello()
h.hello()

print(type(Hello))
print(type(h))

##################################
# metaclass 除了使用type()动态创建类以外，
# 要控制类的创建行为，还可以使用metaclass。
##################################

# metaclass是类的模板，所以必须从`type`类型派生
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass=ListMetaclass):
    pass

##################################
# __new__() 方法接受到的参数依次是:
# 1、当前准备创建的类的对象
# 2、类的名字
# 3、类继承的父类集合
# 4、类的方法集合
##################################


