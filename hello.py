class Person:
    def __init__(self, name , age):
        self.name = name
        self.age = age

    def myf(self):
        print('hello my frend ' + self.name )

    def ages(self):
        print('your age ' + str(self.age))

p1 = Person('xom xom', 16 )
p1.myf()
p1.ages()


