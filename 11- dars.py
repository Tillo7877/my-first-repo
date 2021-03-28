# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 15:02:59 2021

@author: Ismatillayev Hikmatillo
11-dars
"""

#Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!",
#agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.

# son = int(input("juft son kiriting:\n>>>"))
# if son%2==0:
#     print("rahmat")
# else:
#     print("bu juft son emas")


#Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
#◦Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
#◦Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
#◦Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm

# yosh = int(input("yoshingizni kiriting:\n>>>"))
# if yosh<=4 or yosh>=60:
#     print("bepul")
# elif yosh<18:
#     print("10000 so'm")
# else:
#     print("20000 so'm")
    

#Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va 
#ularning teng yoki katta/kichikligi haqida xabarni chiqaring

# print("2 ta son kiriting!")
# son1 = float(input("1-sonni kiriting:\n>>>"))
# son2 = float(input("2-sonni kiriting:\n>>>"))
# if son1 > son2:
#     print(f"{son1} > {son2}")
# elif son1 < son2:
#     print(f"{son1} < {son2}")
# else:print("bu sonlar teng!")


#•mahsulotlar  degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. 
#Yangi, savat  degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang.
#Savatdagi elementlarni, mahsulotlar  ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa 
#"Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.

# mahsulotlar = ['un', 'yog\'', 'non', 'shakar', 'olma', 'o\'rik', 'guruch', 'makron', 'go\'sht', 'tuxum']
# savat = []
# for n in range(5):
#     savat.append(input(f"{n+1}-maxsulotni kiriting:\n>>>"))
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"{mahsulot} bizda bor!")
#     else:
#         print(f"{mahsulot} bizda yo'q!")


#Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang. 
#Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang, bor_mahsulotlar  degan ro'yxatga, 
#do'konda yo'q mahsulotlarni esa mavjud_emas  degan ro'yxatga qo'shing.  Agar mavjud_emas ro'yxati bo'sh bo'lsa,
#"Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda esa
#"Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.

# savat = []
# for n in range(5):
#     savat.append(input(f"{n+1}-maxsulotni kiriting:\n>>>"))
# magazin =[ 'un', 'yog\'', 'non', 'shakar', 'olma', 'o\'rik', 'guruch', 'makron', 'go\'sht', 'tuxum']
# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in magazin:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
# if mavjud_emas:
#     print(f"quyidagi mahsulotlar bizda yo\'q: {mavjud_emas}")
    
# else:
#  print("Siz so'ragan barcha mahsulotlar do'konimizda bor")


#foydalanuvchilar  degan ro'yxat tuzing, va kamida 5 ta login qo'shing. Foydalanuvchidan yangi login 
#tanlashni so'rang va foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning tarkibi bilan 
#solishtiring. Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!"
#aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.         

# foydalanuvchilar = ['botir', 'ali', 'vali', 'anvar', 'abbos']
# login = input("login tanlang:\n>>>")
# if login in foydalanuvchilar:
#     print("login band!")
# else:
#     print(f"{login}, xush kelibsiz")


#Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni
# 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring.

butun_son = int(input("butun son kiriting:\n>>>"))
sonlar = list(range(2, 11))
for son in sonlar:
    if not butun_son%son:
        print(f"{butun_son} {son} ga qoldiqsiz bo'linadi")
       
        




















