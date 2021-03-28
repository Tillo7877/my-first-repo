# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 10:53:09 2021

@author: Ismatillayev Hikmatillo 
10- dars: if operatori
"""
#Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']  degan ro'yxat tuzing, 
#ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.

cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
   if  car == 'gm':
       print( car.upper())
   else:
       print (car.title())
   
 #Yuqoridagi mashqni teng emas (!= ) operatori yordamida bajaring.   

cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
   if  car != 'gm':
      print (car.title())
   else:
       print (car.upper())

#Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. 
#Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring.
# Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}! "  matnini konsolga chiqaring.

login = input("loginni kiriting:\n>>>")
if login.lower() == 'admin':
    print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
    print(f"Xush kelibsiz, {login.title()}!")
    
#Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, 
#"Sonlar teng" ekan degan yozuvni konsolga chiqaring.
print("iltimos 2 ta son kiriting:")
son1 = int(input("1-son:\n>>>"))
son2 = int(input("2-son:\n>>>"))

if son1 == son2:
    print("sonlar teng!")
    
#Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son", 
#agar musbat bo'lsa "Musbat son" degan xabarni chiqaring.    

son = int(input("istagan soningizni kiriting:\n>>>"))

if son < 0:
    print("manfiy son")
else:
    print("musbat son")
    
#Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring.
# Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring.
sonn = int(input("son kiriting:\n>>>"))
if sonn > 0:
    print(sonn**(1/2))
else:
    print("musbat son kiriting!")


