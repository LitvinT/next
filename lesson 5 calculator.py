f_num = float(input('Введите число'))
pro = input('Введите операцию')
s_num = float(input('Введите второе число'))
if pro == '+':
    print(f_num + s_num)
elif pro == '-':
    print(f_num - s_num)
elif pro == '*':
    print(f_num * s_num)
elif pro == '/':
    print(f_num / s_num)
else:
    print('Error')
input()
