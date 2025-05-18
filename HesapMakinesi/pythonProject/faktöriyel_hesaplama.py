
sayi = int(input("Bir sayı giriniz: "))  # Kullanıcıdan sayı al
faktoriyel = 1  # Başlangıç değeri 1 olmalı

for i in range(1, sayi + 1):  # 1'den girilen sayıya kadar döngü
    faktoriyel = faktoriyel * i  # Her seferinde çarparak ilerle

print(f"{sayi}! = {faktoriyel}")  # Sonucu yazdır
