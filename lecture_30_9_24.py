### OOP: Object Oriented Programming  #####
import os.path


def calculate_area(radius):
    return 3.14 * radius ** 2

print("Area:" , calculate_area(5))

# functionlar genledir metotlar objeye özeldir.
# burda da class in icindeki fonksiyondur calculate_area ise bir metottur
# classlar objelerin krokisi bir taslagidir.
#

class Circle:
    pi = 3.14
    def __init__(self, radius):    #burdaki self?
        self.radius = radius
    def calculate_area(self):
        return self.radius ** 2 * Circle.pi


circle= Circle(5)
print("Area:" , circle.calculate_area())


#genelde class isimleri buyuk harfle baslar.
#pascal case denilen isimdeki her kelimenin basi buyuk harfle baslar

class Villa:
    pass

my_villa = Villa()     # object instantiation
print(type(my_villa))  #herhangi bir sekle cevirmediginde kendi icinde bir sey tanimlar ve onun tipini ve adresini basar.

isinstance(my_villa, Villa)  # bu fonksiyondur ve ojenin classa ait olup olmadigini sorgular.


### Constructor Methods  ###

# Dunder Method: Yani D(ouble)Under python da öyzel fonsiyonu olan methodlardir. __init__() örnegindeki gibi basina ve sonuna iki tane underline konur.

# class i olustururken ilerde olusacak objelere gore tasarlarsin. Olmasi gereken özellikler (attributes) gibi...
# burdaki init ile baslyan sey aslinda bir constructor medthod tur. yani obje oluturmak icin özellileri tanimlama islemlerinin oldugu safhadir.

class Person:
    def __init__(self, name, age):      #constructor method
        print("Person object is created")
        self.name = name
        self.age = age

    def display_info(self):   #person classsindan olusturulan objelere ait methodtur
        print(f"Name: {self.name} Age: {self.age}")

    def run(self):
        print("Running...")

person1 = Person("Rabia",27 )
isinstance(person1, Person)

# objelerin özellilerini cagirma, ögrenme
# attribute leri parantezle cagirmayiz

person1.name
person1.age

# class icinde sadece attribute degil action da tanimlanabilir.


person1.display_info()   # object seviyesinde method cagirma, bunu da self saglar


class DataFrame():
    def __init__(self, columns):
        self.columns = columns
        self.data = []
    def insert(self, data_row):
        self.data.append(data_row)
    def show(self):
        print(self.data)

    def head(self):
        pass


# Instance Attributes vs Class Attributes
# Attribute lerin seviyeleri vardir. yani class seviyesinde ve obje seviyesindedir.
# obje tanimlanirken eklenenlere instance attr. denir.
# class attr. ise obje tanimlamadan once yani methodlarin disinda tanimlanan attr. lerdir.


### OOP Concepts
# -Inheritance  : Kalitim, yani bir siniftan baska bir sinif kalitimla özelliklerini devralabilir. hiyerarsi olusumunu saglar.
# --->Parent Class(Base Class) ve Child Class(Derived Class)

class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"Animal Speaks...")

dog_1= Animal("Köpek")
dog_1.speak()

class Dog:
    def havla(self):
        print(f"Köpek Havliyor...")

class Cat:
    def miyav(self):
        print(f"Kedi Miyavliyor...")







# -Encapsulation : siniftaki verilere disaridan erisime kapatip öyel methodlarla kontrol etme
# -Polymorphism : Farkli siniflarin ayni adli methodlari calistirilmasini saglar. Ayni adli methodun farkli siniflarda farkli davranis sergilemesi
# -Abstraction : soyutlama, yani gereksiz detaylari saklayip gerekli bilgilerin gösterilmesi



# Modülleri import icin yapilmasi gereken adimlar.
# Cünkü python default dosyalarindan modül import eder ama biz modülün oldugu path i eklersek python oraya da bakmak zorunda kalir.
import sys
sys.path
import os

os.getcwd() #modele_dosyasi

os.path.join(os.getcwd(), "C:/Users/User/git/deneme_eurotech/lecture_30_9_24.py")

path_to_add

sys.path.append(path_to_add)

