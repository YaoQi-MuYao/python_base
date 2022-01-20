##################################
# 模块
##################################

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello World!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()

##################################
# 作用域
# 正常的函数和变量名是公开的（public），可以被直接引用
# 类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途
# 类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用
# Python并没有一种方法可以完全限制访问private函数或变量
##################################

def _private_1(name):
    return 'Hello %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)




