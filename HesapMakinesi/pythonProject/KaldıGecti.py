
# vize = float(input("Lütfen vize notunuzu giriniz. "))
# final = float(input("Lütfen final notunuzu giriniz. "))
#
# sonuc = ((vize*40)/100) + ((final*60)/100)
#
# if sonuc >= 60:
#     print("Sınavdan gectinizzz. Tebriklerrrr!!! " + "Notunuz = " + str(sonuc))
#
# else:
#     print("Sınavdan kaldınız :( " + "Notunuz= " + str(sonuc))


# NONE

yas = None

while yas is None:
    try:
        yas = int(input("Lütfen yaşınızı giriniz: "))
    break
    except ValueError:
    print("Tekrar deneyiniz")

print(f"Yasınız {yas} olarak kaydedildi")
