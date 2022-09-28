f_num = float(input('Введите число'))
oper = input('Введите операцию')
s_num = float(input('Введите второе число'))
if oper == '+':
    print(f_num + s_num)
elif oper == '-':
    print(f_num - s_num)
elif oper == '*':
    print(f_num * s_num)
elif oper == '/':
    print(f_num / s_num)
else:
    print('Error')
input()
