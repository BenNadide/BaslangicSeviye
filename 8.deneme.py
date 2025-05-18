
while True:
 try:

    prime = True
    sayi = input("Bir sayi giriniz(Çıkmak isterseniz q'ya basın): ")

    if sayi.lower() == 'q':
        print("Çıkılıyor...")
        break

    sayi = int(sayi)

    for i in range(2, sayi):
        if (sayi % i == 0):
            prime = False
            break

    if not prime or sayi<=0:
        print("Asal değil\n")
    else:
        print("Asal\n")



 except ValueError:
     print("Hatalı giriş! Tekrar deneyin\n")