n = int(input('numer:'))

users = {
    i: {
        'name': input(f'{i} name:'),
        'email': input(f'{i} email')
    } for i in range(n)
}
print(users)
