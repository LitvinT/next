def ram(x):
   print ('квадрат числа', x, '=', x**2)
ram(5)

def multi(a,b):
    print(a*b)
multi(8,9)

def even (a):
        if a%2==0:
            print(a,'четное')
        else:
            print(a, 'не четное')
for i in range(30,40,3):
    even(i)

def factorial(n):
    pr=1
    for i in range(2,n+1):
       pr=pr*i
    print(pr)

if 5>6:
    def primer():
        print('hello')
else:
    def primer():
        print('HELLO')

primer()