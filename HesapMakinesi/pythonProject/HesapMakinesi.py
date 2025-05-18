# HESAP MAKİNESİ

import math

while True:
    try:
        x = float(input("Lütfen ilk sayı değerini giriniz. "))
        y = float(input("Lütfen ikinci sayı değerini giriniz. "))

        break

    except ValueError:
        print("Hata!! Lütfen tekrar deneyiniz. ")


print("\nSon olarak yapmak istediğiniz işlemi seçin:")
print(" - Çarpma: c")
print(" - Bölme: b")
print(" - Toplama: t")
print(" - Çıkarma: e")
print(" - Karekok: k")
print(" - Üssü: u")


while True:
    islem = input("Seçiminizi yapınız: ").lower()

    if islem not in ["c","b","t","e","k","u"]:
        print("Hata: Geçersiz giriş yaptınız, tekrar deneyin.")

    else:
        break

if islem == "c":
    print(f"Sonuç: {x * y}")

elif islem == "b":
    if y == 0:
        print("Hata: Sıfıra bölme yapılamaz!")
    else:
        print(f"Sonuç: {x / y}")

elif islem == "t":
    print(f"Sonuç: {x + y}")

elif islem == "e":
    print(f"Sonuç: {x - y}")

elif islem == "k":
    if x < 0:
        print("Hata: Negatif sayının karekökü alınamaz!")
    else:
        print(f"{x} sayısının karekökü: {math.sqrt(x)}")

elif islem == "u":
    print(f"{x} üzeri {y} = {x ** y}")

