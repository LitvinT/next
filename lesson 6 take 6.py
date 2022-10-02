array = [1,2,3,4,5,6,7,8,9,] # тут список чисел
print(*[x for x in array if not x % 2]) # выводим четные
print(*[x for x in array if x % 2]) # выводим нечетные

