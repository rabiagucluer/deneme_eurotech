#Data Structures
from typing import Tuple

#Strings

str_op = [1, 2, 3, 4]


#String Operations

str1="Hello"
str2="World"

num1="9"
num2="4"

var = num1 + num2 #94

var_2 = str1 + " " + str2 # Hello World

var_3 = str1 * 4

# % Formatting
# str.format()
# f.strings (python 3.6 dan itibaren kullanılıyor)

name = "rabia"
surname = "köme"

#parametize etmek istersek

f"Öğrencinin adı: {name}, öğrencinin soyadı: {surname} "

"Öğrencinin adı: {} , öğrencinin soyadı: {} ".format(name,surname)

#Escape Characters \
print('I\'m Rabia')
#row strings
print(r"I\ m' Rabia")

#String Method

#upper
#lower
#capitalize
#replace
#strip

my_name= "       Engin       "
my_name.upper()
my_name= my_name.replace("E","A")

print(my_name)

my_sent = "Hello World, I came"
my_sent.replace("H","h")
split_ted = my_sent.split(",")
type(split_ted) # output ist list

print(split_ted[0])

#list operations

list1 = [1,2,3,4]
list2 = [5,5,7,8]

con = list1+list2

con2 = list1*3

con3 = 5 in list1
#iç içe list
nested_list=[["a","b","c"],1, False]

new_list= nested_list[0]
print(nested_list[0][2])

# List Methods

first = [1,2]
third = first.copy() # fisrt ü kopyalayıp başka adreste tutar atamadan fasrklı olarak

# shallow copy and deep copy
#Adding
    #append: gelen veriyi sona ekler. eğer birden fazla olursa eklenenleri liste olarak ekler
    #extend: liste birden çok value eklemek istediğimizde kullanılır
    #insert: liste belirli bir yere eklemek istersek kullanırız. index veriririz.
my_list = [1, 2, 3]
my_list.extend([5,6,7]) #listi overwrite eder
my_list.append(8)
my_list.insert(0,"ilk deger")

#Remove Elements
    #remove: listeden ilk gördüğü istenilen elemanı siler aynı elemanın diğerlerini kalır.
    #pop: silmek istediğinin elemanı değil de indexini veririz. o yüzden silmek istediğimiz veriyi de biliyoruz demektir ama bilmesekte sildiği indexi de gösterir.
    # eğer bir index girmezsek en son indexi siler. Silinen indexi bir değişkende tutmak mantıklı olur
    #del: aralık verme imkanı tanır

my_list.remove(3)
deleted_item = my_list.pop(0)
my_list.pop()
del my_list[0:3]

#Sorting

my_list = [1,4,6,7,2,8,9,10,6]
my_list.sort() #sadece listlere özeldir. overwrite eder
sorted(my_list) # bu ise her şeyde kullanılır. overrite etmez
my_list.sort(reverse = True) # tersten sıralar
sorted(my_list, reverse = True)

#reversing
#listeyi tersten yazdırır

reversed_list = my_list[::-1] #overwrite etmedi
my_list.reverse()  #overwrite etti

#Tuple
#Set


