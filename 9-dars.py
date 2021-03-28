# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 09:01:42 2021

@author: Ismatillayev Hikmatillo
9-dars
"""
#Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
#Yuoqirdagi tsikl tugaganidan so'ng, ekranga "Kod n  marta takrorlandi" degan 
#xabarni chiqaring (n  o'rniga kod necha marta takrorlanganini yozing)

ismlar = ['umidjon', 'nasimjon', 'tohirjon', 'ulug\'bek','no\'monjon']
for ism in ismlar:
    print(ism.title(), "bugun futbol!")
print("kod", len(ismlar), "marta takrorlandi")

#10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. 
#Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.

#toq_sonlar = list(range(11,100,2 ))
#for kub in toq_sonlar:
    #print(kub**3)
#Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang,
#va kinolar  degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
kinolar = []
print("5 ta eng sevimli kinolaringizni kiriting:")
for n in range(5):
    kinolar.append(input(f"{n+1} -sevmli kinoingizni kiriting:"))
print(kinolar)

#Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang,
#va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring
n = input("bugun necha kishi bilan suhbatlashdingiz?,\n>>>")
suhbatdoshlar = []
for m in range(int(n)):
    suhbatdoshlar.append(input(f"{m+1}-suhbatdoshingiz ismini kiriting:"))
print(suhbatdoshlar)



