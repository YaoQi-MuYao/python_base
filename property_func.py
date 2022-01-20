##################################
# @property
##################################

class Student(object):
     def get_score(self):
         return self._score

     def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('必须是整数')
        if value < 0 or value > 100:
            raise ValueError('必须在0 ~ 100之间')
        self._score = value

s = Student()
s.set_score(60)
print(s.get_score())

s.set_score(999)
print(s.get_score())

# 其实可以使用@property注解简化操作
# 特别需要注意的一点属性的方法名不要和实例变量重名 ，如果只定义一个 @property的属性方法 那么该属性是只读属性
class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth

