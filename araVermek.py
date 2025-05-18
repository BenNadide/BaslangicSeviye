import random

sayi = random.randint(1, 10)
sayac = 0
print("Bir sayı tuttum. Tahmin ett!!")

while True:
    tahmin = int(input("Tahminin: "))
    sayac = sayac + 1

    if sayac == 3:
        print(f"Tahmin hakkınız bitti. cevap {sayi} idi.")
        break
    else:
        if tahmin < sayi:
            print("Biraz daha büyük bir sayı girin.")
        elif sayi < tahmin:
            print("Biraz daha küçük bir sayı girin.")
        else:
            print("Doğru bildinizzzz")
            break
