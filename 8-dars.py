# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 15:56:00 2021

@author: Ismatillayev Hikmatillo
dars-8!
"""

#O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring

davlatlar = ['uzb', 'kz', 'aqsh', 'rus', 'kg', 'turk']
print('1',davlatlar)

#Ro'yxatning uzunligini konsolga chiqaring

print('2',len(davlatlar))
#sorted()  funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring

print('3',sorted(davlatlar))

#sorted()  yordamida ro'yxatni teskari tartibda konsolga chiqaring

print('4',sorted(davlatlar, reverse =True ))

#Asl ro'yxatni qaytadan konsolga chiqaring

print('5',davlatlar)

#reverse()  metodi yordamida ro'yxatni ortidan boshlab chiqaring

davlatlar.reverse()
print('6', davlatlar)

#sort()  metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.

davlatlar.sort()
print('7', davlatlar)
davlatlar.reverse()
print('8',davlatlar)

#120  dan 1200  gacha bo'lgan juft sonlar ro'yxatini tuzing

juft_sonlar = list(range(120,1202,2))
#print(juft_sonlar)

#Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring

yigindi = sum(juft_sonlar)
print("yig'indi:",yigindi)

#Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring

kattasi = max(juft_sonlar)
kichigi = min(juft_sonlar)
print("ayirma:", kattasi-kichigi)

#Ro'yxatdagi elementlar sonini hisoblang

print("elementlar soni:",len(juft_sonlar))
#Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
print(juft_sonlar[:20], " \t\t\t", juft_sonlar[541//2-10:541//2+10],"\t\t\t", juft_sonlar[541-20:])

#taomlar  degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting

taomlar = ['osh', 'chuchvara', 'manti', 'xunon', 'dimlama' ]
#nonushta  degan yangi ro'yxatga taomlar dan nusxa oling

nonushta = taomlar[:]
#Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing

nonushta.remove("xunon")
nonushta.remove("manti")
nonushta.remove("dimlama")
nonushta.append("saryog'")
nonushta.append("shakar")

#Ikkala ro'yxatni ham (taomlar  va nonushta ) konsolga chiqaring
print(nonushta)
print(taomlar)

#Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va 
#nonushta[0] = "qaymoq va non"  deb qiymat berib ko'ring.

#nonushta = tuple(nonushta)
#nonushta[0] = "qaymoq va non"




