sonuc = None
while True:
    try:
        sayi1 = input("İlk sayiyi girin (çıkmak ıcın q ya basın): ")

        if sayi1 == 'q':
            print("Çıkılıyor...")
            break
        else:
            sayi2 = float(input("İkinci sayiyi girin: "))
            sayi1 = float(sayi1)
            islem = input("Yapmak istediğiniz islemi secin (*,/,-,+): ")
            if islem not in ['+', '-', '*', '/']:
                print("Geçersiz işlem! Lütfen +, -, *, / girin.")
                continue
            elif islem == '*':
                sonuc = sayi1 * sayi2
                print(sonuc)
            elif islem == '/':
                sonuc = sayi1 / sayi2
                print(sonuc)
            elif islem == '-':
                sonuc = sayi1 - sayi2
                print(sonuc)
            elif islem == '+':
                sonuc = sayi1 + sayi2
                print(sonuc)

    except ValueError:
        print("Lütfen gecerli karakteri girin!")
    except ZeroDivisionError:
        print("İkinci sayi sifir olamaz")




# try:
#     islem = input("İşlem girin (+, -, *, /): ")
#     if islem not in ['+', '-', '*', '/']:
#         raise ValueError("Geçersiz işlem seçildi.")
#
#     x = float(input("Birinci sayı: "))
#     y = float(input("İkinci sayı: "))
#
#     if islem == '+':
#         print("Sonuç:", x + y)
#     elif islem == '-':
#         print("Sonuç:", x - y)
#     elif islem == '*':
#         print("Sonuç:", x * y)
#     elif islem == '/':
#         print("Sonuç:", x / y)
#
# except ValueError as hata:
#     print("Hata:", hata)
# except ZeroDivisionError:
#     print("0'a bölme hatası! Lütfen ikinci sayıyı 0 dışında girin.")

# ----------------------------------------------------------------------------------------------------------------------

# while True:
#     try:
#         sayi1 = input("İlk sayıyı girin (çıkmak için 'q' tuşlayın): ")
#
#         if sayi1.lower() == 'q':  # Harf büyük girilirse de çalışsın
#             print("Çıkılıyor...")
#             break
#
#         sayi1 = float(sayi1)  # Sayıya çevir
#         sayi2 = float(input("İkinci sayıyı girin: "))
#
#         islem = input("İşlem seçin (+, -, *, /): ")
#         if islem not in ['+', '-', '*', '/']:
#             print("❌ Geçersiz işlem! Lütfen +, -, *, / girin.\n")
#             continue  # Başa dön
#
#         if islem == '+':
#             sonuc = sayi1 + sayi2
#         elif islem == '-':
#             sonuc = sayi1 - sayi2
#         elif islem == '*':
#             sonuc = sayi1 * sayi2
#         elif islem == '/':
#             sonuc = sayi1 / sayi2
#
#         print("✅ Sonuç:", sonuc, "\n")
#
#     except ValueError:
#         print("❗ Lütfen geçerli bir sayı girin.\n")
#     except ZeroDivisionError:
#         print("❗ 0'a bölme hatası! İkinci sayı sıfır olamaz.\n")
