def mutate(lst):
    list = lst[::-1]
    lst.clear()
    lst.extend(list)

a = [1,2,3,4]
print(a)
mutate(a)
print(a)
#mutate Функция создает обратную копию своих входных данных



x = [1,2,3,4,5,6,7,8,9,10]

z = []

for i in range(len(x)):
    m = len(x) - i -1
    z.insert(i,x[m])

print(z)