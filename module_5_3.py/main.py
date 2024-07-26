class House:
    def __init__(self,name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self,new_floor):
        if 1<= new_floor <= self.number_of_floors:
            for floor in range (1,new_floor +1):
                print("Такого этажа не существует", self.name)
            else:
                print(new_floor)

    def __str__(self):
        return f"Название:{self. name}, кол-во этажей:{self.number_of_floors}"
    def __len__(self):
        return self.number_of_floors
    def __ed__(self, other):
        return self.number_of_floors == other.number_of_floors
    def __it__(self, other):
        return self.number_of_floors < other.number_of_floors
    def __le__(self,other):
        return self.number_of_floors <=other.number_of_floors
    def __gt__(self,other):
        return self.number_of_floors > other.number_of_floors
    def __ne__(self, other):
        return self.number_of_floors!= other.number_of_floors
    def __add__(self, value):
       if isinstance(value, int):
           return self.number_of_floors + value
       print(h1. __str__())
       return f"Название:{self.name}, кол-во этажей:{self.number_of_floors}"

    def __iadd__(self, value):
        if isinstance(value,int):
            return self.number_of_floors + value
        print(h1.__str__())

        return f"Название:{self.name}, кол-во этажей:{self.number_of_floors}"
    def __radd__(self, value):
        if isinstance(value,int):
            return self.number_of_floors + value
        print(h2.__str__())

        return f"Название:{self.name}, кол-во этажей:{self.number_of_floors}"


h1=House("ЖК Эльбрус",10)
h2=House("ЖК Акация",20)
print(h1)
print(h2)

print(h1==h2)
h1=h1+10
print(h1)

print(h1==h2)
h1+=10
print(h1)

h2=10+h2
print(h2)

print(h1>h2)
print(h1>=h2)
print(h1<h2)
print(h1<=h2)
print(h1!=h2)