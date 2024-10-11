### MODUL AND PACKAGE
# modül : file
# package: folder
import importlib
# Modülleri import icin yapilmasi gereken adimlar.
# Cünkü python default dosyalarindan modül import eder ama biz modülün oldugu path i eklersek python oraya da bakmak zorunda kalir.

import sys
sys.path

import os
import os
os.getcwd() #modele_dosyasi

os.path.join(os.getcwd(), "C:/Users/User/git/deneme_eurotech/lecture_30_9_24.py")


path_to_add
sys.path.append(path_to_add)

import datetime
datetime.datetime.now()

import random
random.randint(1,100)

import math
# from math import sqrt
math.sqrt(4)

import json

# eger bir modül halihazirda import edilmisse tekrar import etmez. degisimi yeniden tanitmamiz gerek bu nedenle asagidaki kod parcasi kullanilir
importlib.reload(math_op)  # modelün adi yazilir ice

# kodlar bir script olarak bir de modül olarak calistirilabilir.
# fark ise script -->main olarak run eder
#          modül --> dosya ismi neyse onu run  eder

# bu farkli run etme sebebi developer in herkesin görmesini istemedigi kodlari calistirmak istemesinden kaynaklidir
# görülmesi istenilmeyen kisimlar if statement ta calisir

if (__name__ == "__main__"):  ## script olarak calirsa bu kisim oluyor
    print("Hosgeldin")
else:
    print("import edildi")   ## modül olarak calisirse bu kisim


### Package
# __init__.py diye bir file vardir package icinde. package i package yapan bu init dosyasi denebilir. init olmadan package olarak kabul edilmez.
# bir package icine hem modül hem bir package ekledigimizi varsayalim. ana package package_1 olsun alt package ise package_2 olsun
# bunlari su sekilde import ederiz:
# from package_1 import module_1
# from package_1 import package_2
# from package_1.package_2 import module_2.... gibi gibi

## pip install ... yuklemek istedigin package veya modulü indirecegi adrese gider.
## sirketlerin ise bir repo da saklidir. Onlari ise söyle import ederiz: pip install --index--url "I can give my own private repo". url ye package in oldugu repo nun adresi eklenir



