a = float(input('Число '))
c = input('Введите операцию ')
v = float(input('Число '))
if c == '+':
    print(a + v)
elif c == '-':
    print(a - v)
elif c == '*':
    print(a * v)
elif c == '/':
    print(a / v)
else:
    print('Error')
