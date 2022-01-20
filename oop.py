##################################
# 面向对象
##################################

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))




muYao = Student('MuYao', 99)
wenRuo = Student('WenRuo', 99)
muYao.print_score()
wenRuo.print_score()
