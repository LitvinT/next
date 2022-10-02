numbers = [1, 2, 4, 5, 7, 8, 10, 11]
filtered = [] # список, содержащий отфильтрованные элементы
for element in numbers :
    if not element % 2:
        filtered.append(element)
print(filtered) # отображаем результат