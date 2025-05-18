import math
while True:
    try:

        devam = input("Çıkmak isterseniz q'ya devam etmek isterseniz c'ye basın: ")
        if devam.lower() == 'q':
            print("Çıkılıyorrr...")
            break
        elif devam.lower() == 'c':
            aci = int(input("Üçgenin iki kenar arasındaki açısını giriniz: "))
            kenar1 = int(input("Birinci kenar ölçüsü: "))
            kenar2 = int(input("İkinci kenarı giriniz: "))
            from math import sin
            alan = kenar1 * kenar2 * (sin(aci)/2)
            print(f"Sonuç: {alan}")
        else:
            if devam not in ['q', 'c']:
                raise ValueError("Geçersiz giriş! Sadece 'q' veya 'c' kabul edilir.")
                continue
    except ValueError:
        print("Hatalı giriş yaptınız. Tekrar deneyin!")

