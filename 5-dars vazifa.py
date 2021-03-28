# sariq.dev 5-dars
"""
o'rganuvchi Ismatillayev

9.03.2021
"""
#1# Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
# Diqqat uzun kodlarni \ belgisi yordamida keyingi qatorga
# ko'chirish mumkin
#kocha = "Bog'bon" 

#mahalla = "Sog'bon" 

#tuman = "Bodomzor"  

#viloyat = "Samarqand" 

#print(kocha+" ko\'chasi,", mahalla+" mahallasi,", tuman+" tumani,", viloyat+" viloyati" )

#2#Yuqoridagi o'zgaruvchilarning qiymatini foydalanuvchidan so'rang.
#kocha = input("ko'cha nomini kiriting:\n")

#mahalla = input("mahalla nomini kiriting:\n") 

#tuman = input("tuman nomini kiriting:\n")

#viloyat = input("viloyat nomini kiriting:\n")

#print(kocha.capitalize()+" ko'chasi,", mahalla.capitalize()+" mahallasi,", tuman.title()+ " tumani,", viloyat.title()+" viloyati")

#3333333# Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatorga yozing

#kocha = "Bog'bon" 

#mahalla = "Sog'bon" 

#tuman = "Bodomzor"  

#viloyat = "Samarqand" 

#print( kocha+" ko\'chasi,\n", mahalla+" mahallasi,\n", tuman+" tumani,\n", viloyat+" viloyati") 

#44444444# Yuqoridagi o'zgaruvchilarni f-string yordamida, yangi manzil deb nomlangan o'zgaruvchiga yuklang
#kocha = "bog'bon" 

#mahalla = "sog'bon" 

#tuman = "bodomzor"  

#viloyat = "samarqand" 

#manzil = f" {kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani,  {viloyat} viloyati"
#print(manzil)

#55555#manzil ga biz yuqorida o'rgangan metodlarni qo'llab ko'ring.

kocha = "bog'bon" 

mahalla = "sog'bon" 

tuman = "bodomzor"  

viloyat = "samarqand" 

manzil = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani,  {viloyat} viloyati"

print(manzil.title(),"\n")

print(manzil.capitalize(),'\n')

print(manzil.upper(),'\n')

print(manzil.lower(),'\n')
