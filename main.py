import quard

def print_hi(name):
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


classmates = ['muyao', 'wenruo', 'zhangshuo']
print(classmates[0])
print(classmates[1])
print(classmates[2])
print(classmates[-1])

names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print('Hello ,', name)

if __name__ == '__main__':
    print('line')

quard.quadratic(1, 2, 3)

print('100 + 200 =', 100 + 200)

d = {'muyao' : 1, 'wenruo' : 2}
print('是否存在: ', 'ming' in d)
d['ming'] = 3
print('是否存在: ', 'ming' in d)
print('值: ', d.get('ming'))
