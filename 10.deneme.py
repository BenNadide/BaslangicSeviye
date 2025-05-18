
while True:
    try:
        sayi1 = input("Birinci kenarı giriniz ve çıkmak isterseniz q'ya basın: ")
        if sayi1.lower() == 'q':
            print("Çıkılıyor...")
            break
        sayi1 = int(sayi1)
    except ValueError:
        print("Hatalı giriş!!! Ya sayi girin yada q")
        continue
    while True:
        try:
            sayi2 = int(input("İkinci sayiyi giriniz: "))
            break
        except ValueError:
            print("Hatalı giriş!!! Sadece sayi giriniz.")
            continue

    if sayi2 < sayi1:
        print(f"{sayi1} daha büyük")
    elif sayi1 < sayi2:
        print(f"{sayi2} daha büyük")
    else:
        print("Eşit")