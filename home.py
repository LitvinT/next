class house():
    """описание дома"""
    def __init__(self,stret,number):
        """свойства дома"""
        self.stret = stret
        self.number = number
        self.age = 0

    def build(self):
        """строить дом"""
        print('дом на улице '  + self.stret + ' под номером ' + str(self.number) + ' построен.')
    def age_house(self,year):
        """возраст дома"""
        self.age += year

house1 = house('беды', 2)
house2 = house('беды', 25)


#print(house1.stret,house1.number)
# house2.build()
# house1.age_house(3)
# print(house1.age)
# print(house1.age)
# house1.age_house(5)
# house2.age_house(2)
# print(house1.age)
# print(house2.stret,house2.number,house2.age)
class prospectHouse(house):
    """дома на проспектк"""
    def __init__(self, prospect, number):
        super().__init__(self,number)
        self.prospect = prospect

PrHouse = prospectHouse('Ленина', 7)
print(PrHouse.prospect, PrHouse.number)
