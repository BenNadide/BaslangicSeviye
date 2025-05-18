
while True:
    try:
        now = int(input("Şu anda bulunduğunuz yılı giriniz: "))
        break  # Eğer giriş doğruysa döngüden çık
    except ValueError:
        print("Lütfen geçerli bir yıl giriniz!")  # Hatalı giriş için uyarı mesajı


while True:
    try:
        yas = int(input("Yaşınızı giriniz: "))
        break
    except ValueError:
        print("Lütfen geçerli bir sayı giriniz!")

