bakiye = 5000.0
dogru_pin = 1234
giris_basarili = False

print("=== AKILLI ATM SİSTEMİ ===")

for deneme_sayisi in range(3):

    pin = int(input("PIN kodunuzu giriniz: "))

    if pin == dogru_pin:
        print("Giriş başarılı!")
        giris_basarili = True
        break

    else:
        deneme_sayisi += 1
        kalan_hak = 3 - deneme_sayisi

        print("Hatalı PIN!")
        print("Kalan deneme hakkı:", kalan_hak)
        print()

if giris_basarili == False:
    print("Deneme hakkınız doldu.")
    print("Hesap erişimi engellendi.")

else:
    while True:
        print()
        print("=== AKILLI ATM SİSTEMİ ===")
        print("1 - Bakiye Görüntüleme")
        print("2 - Para Yatırma")
        print("3 - Para Çekme")
        print("4 - Çıkış")

        secim = input("İşlem seçiniz: ")

        if secim == "1":
            print("Mevcut bakiye:", bakiye, "TL")

        elif secim == "2":
            tutar = float(input("Yatırılacak tutar: "))

            if tutar > 0:
                bakiye += tutar
                print("Para yatırma işlemi başarılı.")
                print("Güncel bakiye:", bakiye, "TL")

            else:
                print("Geçersiz tutar!")
                print("Bakiye değişmedi:", bakiye, "TL")

        elif secim == "3":
            tutar = float(input("Çekilecek tutar: "))

            if tutar <= 0:
                print("Geçersiz tutar!")

            elif tutar > bakiye:
                print("Yetersiz bakiye!")
                print("Mevcut bakiye:", bakiye, "TL")

            else:
                bakiye -= tutar
                print("Para çekme işlemi başarılı.")
                print("Güncel bakiye:", bakiye, "TL")

        elif secim == "4":
            print("Çıkış yapılıyor...")
            print("Bizi tercih ettiğiniz için teşekkür ederiz.")
            break

        else:
            print("Geçersiz işlem seçimi!")

print()
print("=== PROGRAM SONU ===")