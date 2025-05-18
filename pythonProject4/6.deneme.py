
z = None
while True:
    x = input("İlk sayıyı giriniz (çıkmak isterseniz q ya basın): ")
    try:
        if x.lower() == "q":
            print("Çıkılıyor...")
            break
        else:
            y = float(input("İkinci sayıyı giriniz: "))
            x = float(x)
            z = x / y
    except(ValueError,ZeroDivisionError):
        print("Tekrar deneyin")

#
# while True:
#     try:
#         x = float(input("Bir sayı girin: "))
#         y = float(input("İkinci sayı: "))
#         sonuc = x / y
#     except ValueError:
#         print("Sayı girmeniz gerekiyor. Tekrar deneyin.")
#         continue  # 🔁 başa dön
#     except ZeroDivisionError:
#         print("0'a bölme hatası. Lütfen farklı bir sayı girin.")
#         continue
#     else:
#         print("Sonuç:", sonuc)
#         break

