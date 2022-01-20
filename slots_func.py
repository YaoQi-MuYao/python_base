##################################
# slots 限制类的属性
##################################

from types import MethodType

class Student(object):
    pass

# 动态的给实例绑定一个属性
s = Student()
s.name = 'Michael'
print(s.name)

# 动态的给实例绑定方法
def set_age(self, age):
    self.age = age

s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)

# 但是给一个实例绑定了方法 另一个实例无法使用
s2 = Student()
# s2.set_age(25) # 这里会报异常

# 如果想给所有的实例绑定方法
def set_score(self, score):
    self.score = score

Student.set_score = set_score

s.set_score(20)
print(s.score)
s2.set_score(100)
print(s2.score)

# 使用 __slots__ 限制类的属性
class Student(object):
    __slots__ = ('name', 'age')

