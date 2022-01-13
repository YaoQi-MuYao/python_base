##################################
# 返回函数
##################################

# 函数返回结果为函数
def lazy_sum(*args):
    print('args参数', args)
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum


sum = lazy_sum(1,3,5,7)
# sum = lazy_sum(list(range(20)))
print(sum())