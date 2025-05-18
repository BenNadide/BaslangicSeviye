
urunler = {} #sözlük ismi

while True:
    urun_adi = input("ÜRÜN ADI (bitirmek için 'bitti'): ")
    if urun_adi == "bitti":
        break
        fiyat = float(input(f"{urun_adi.capitalize()} fiyatı = "))
        urunler[urun_adi] = fiyat

print("\nAlışveriş Listesi:")

for urun,fiyat in urunler.items():
    print(f"{urun.capitalize()} - {fiyat} TL")
