
# range() kullanımı

# ÖRNEK 1
# sayilar = range(23) # 23 dahil değil
# print(list(sayilar))

# ÖRNEK 2
# sayilar = range(10,25) # 25 dahil değil
# print(list(sayilar))

# list i eklemeyince range(10,25) seklinde olduğu gibi yazıyor.

# ÖRNEK 3
# sayilar = range(10,25,2)
# print(list(sayilar))

# ÖRNEK 4
# sayilar = range(20,9,-3)
# print(list(sayilar))

###################################################################

# Şimdi ise for ile kullanımına bakalım

# for deger in range(11):
#     print(deger * deger)

#------------------------------------------------------------------

# for deger in range(11):
#     print(deger)

# sayi = int(input("Bir sayı giriniz = "))
#
# for sayi in range(sayi):
#     print(sayi)
#
# print(sayi)

# üstteki kod hatalı yazım for i in range seklinde yazıp print(i) olması gerekirdi yoksa hata olur anlamadıysan tkr araştır
#Doğrusu şöyle

# sayi = int(input("Bir sayı giriniz. "))
# for i in range(sayi):
#     print(i)

#doğrusu böyledir ve en son kontrol etmek istersen print(sayi) yazıp saqyi değişkeninin kullanıcıdan aldığı değeri hala koruduğunu görebilirsin

# sayi = int(input("Bir sayı giriniz. "))
# toplam = 0
# for i in range(sayi+1):
#  toplam = toplam + i
#  print(toplam)

# ----------------------------------------------------------------------

# isim = (input("Bir isim giriniz = "))
#
# for i in range(10):
#     print(isim)

# isim = "yazılımkodlama"
# for i in isim:
#     print(i)


# - REVERSED -
# isim = input("Bir isim giriniz ")
# for i in reversed(isim):
#     print(i)

# x = ["Antalya","İstanbul","İzmir","Ordu","Bursa"]
# # for i in x:
# #     print(i)

# for i in x:
#     print(f"{i} sehri {len(i)} karakterden olusuyor")

# for i in x:
#     if len(i) == 5:
#         print(i)

# sayilar = ["12","43","11","56","43","12","8","6","21"]
#
# # for i in sayilar:
# #     if int(i)%2 != 0:
# #         print(f" listedeki tek sayılar = {i}")
#
# toplam = 0
# for i in sayilar:
#     if int(i) % 2 == 0:
#         toplam = toplam +int(i)
# print(toplam)
