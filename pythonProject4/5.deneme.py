import math

while True:

    ilk_kenar = input("Lütfen dik üçgenin bir kenarını giriniz(çıkmak istersenız q ya basın): ")
    ikinci_kenar = input("Lütfen dik üçgenin ikinci kenarını giriniz: ")


    if ilk_kenar.lower() == 'q':
        print("Çıkılıyor...")
        break

    if not (ilk_kenar.replace('.','',1).isdigit() and ikinci_kenar.replace('.','',1).isdigit()):
        print("Lütfen geçerli bir sayı girin veya çıkmak için 'q' tuşlayın.\n")
        continue

    ilk_kenar = float(ilk_kenar)
    ikinci_kenar = float(ikinci_kenar)
    sonuc = 0

    sonuc = (ilk_kenar ** 2) + (ikinci_kenar ** 2)

    from math import sqrt
    print(math.sqrt(sonuc))


