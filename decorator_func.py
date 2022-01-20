##################################
# 装饰器
##################################

# 装饰器 decorator
# def now():
#     print('2022-01-18')
#
#
# f = now
# print(now.__name__)
# print(f.__name__)
import functools


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*agr, **kw):
            print('%s %s()' % (text, func.__name__))
            return func(*agr, **kw)
        return wrapper
    return decorator


@log('wen ruo')
def now():
    print('2022-01-18')

now()

print(now.__name__)

