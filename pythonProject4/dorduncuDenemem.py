
pi = 3.14

while True:
    radius = input("Lütfen kürenin yarıçapı girin (çıkmak isyerseniz q ya basın) ")

    if radius == 'q':
        print("çıkılıyor...")
        break
    else:
        radius = float(radius)
        alan = 4 * pi * (radius ** 2)
        hacim = 4 / 3 * pi * (radius ** 3)
        print(f"alan: {alan}, hacim: {hacim}")
