
while True:
    veri = input("Mil'e cevirmek istediğiniz değeri giriniz ve cıkmak isterseniz 'q' basın: ")

    if veri.lower() == 'q':
        print("Çıkılıyor...")
        break
    elif not veri.replace('.', '', 1).isdigit():
        print("Lütfen geçerli bir sayı girin veya çıkmak için 'q' tuşlayın.\n")
        continue

    veri = float(veri)
    veri = veri / 1.609344
    print(veri)






