# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 11:15:05 2021

@author: Ismatillayev Hikmatillo
dars-7... vazifa 1--
"""
#ismlar  degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting

ismlar = ['Botirjon', 'Tohirjon', 'Ixtiyor']
#Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring:
print(ismlar[0],", bugun futbol!")
print(ismlar[1],", bugun osh!")
print(ismlar[2],", bugun dam!")

#sonlar  deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik). 

sonlar = [1, -7, 5, 9.9]

#Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring.
#Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring.


print(sonlar)
print(sonlar[0]+sonlar[3])
print(sonlar[1]-sonlar[2])
print(sonlar[2]*sonlar[2])
print(sonlar[2]+sonlar[1])
sonlar[0] = 15
sonlar[2] = 11.1
print(sonlar)


#t_shaxslar va z_shaxslar  degan 2 ta ro'yxat yarating va biriga o'zingiz 
#eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi 
#tirik bo'lgan shaxslarning ismini kiriting

t_shaxslar = ['Muhammad S.A.V', 'Abu Bakr r.a', 'Umar r.a', 'Usmon r.a', 'Ali r.a']
z_shaxslar = ['Kusherbayev', 'Xushnud', 'Begzod']

#Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop() ), 
#quyidagi ko'rinishda chiqaring:

print("Men tarixiy shaxslardan", t_shaxslar.pop(0), " bilan,\n", 
      "zamonaviy shaxslardan esa", z_shaxslar.pop(2), "bilan\n suhbatlashishni istardim..." )

#friends nomli bo'sh ro'yxat tuzing va unga .append()  yordamida 5-6 ta 
#mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.

friends = []
print(friends)
friends.append('Botirjon')
friends.append('Islomtoy')
friends.append('Ixtiyor')
friends.append('Hojiakbar')
friends.append('Abdurahim')
print(friends)

#Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove()  metodi yordamida o'chrib tashlang.

friends.remove('Ixtiyor')
friends.remove('Hojiakbar')
print(friends)

#Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.

friends.append('Tohirjon')
friends.insert(1,'Abbos')
friends.insert(0,'Abduholiq')
print(friends)

#Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop()  va .append() \
#metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends \
#ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.

mehmonlar = []
print(mehmonlar)
mehmonlar.append(friends.pop(3))
mehmonlar.append(friends.pop(-1))
mehmonlar.append(friends.pop(0))
print(mehmonlar)



