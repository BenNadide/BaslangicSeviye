
while True:

 try:

    miktar = input("Kaç tane asal sayı istersiniz(Çıkmak isterseniz q'ya basın): ")
    if miktar == 'q':
        print("Çıkılıyor...")
        break

    miktar = int(miktar)
    sayi = 2
    asal_sayi_sayaci = 0
    kutu = []

    while len(kutu) <= miktar:
        for i in range(1,100):
            if (sayi % i == 0):
                kutu.append(sayi)
                sayi = sayi + 1


 except ValueError:
     print("Hatalı giriş!!\n")

