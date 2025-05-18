alan = 0
cevre = 0
while True:
    kenar = input("Karenin kenarını giriniz(bitirmek istersen iz 'q' ya basın: ")

    if kenar == 'q':
        print("Bitiriliyor")
        break
    else:
        kenar = float(kenar)
        alan = kenar ** 2
        cevre = kenar * 4

        print(f"Alan = {float(alan)}, Cevre = {float(cevre)}")


