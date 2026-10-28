# Başlangıç bilgileri
bakiye = 5000.0
dogru_pin = "1234"

print("=== AKILLI ATM SİSTEMİ ===")

pin = input("PIN kodunuzu giriniz: ")

if pin == dogru_pin:
    print("Giriş başarılı!")

    print("\n1 - Bakiye Görüntüleme")
    print("2 - Para Yatırma")
    print("3 - Para Çekme")

    secim = input("\nİşlem seçiniz: ")

    if secim == "1":
        print("Mevcut bakiye:", bakiye, "TL")

    elif secim == "2":
        tutar = (input("Yatırılacak tutar: "))

        if tutar > 0:
            bakiye += tutar
            print("Para yatırma işlemi başarılı.")
            print("Güncel bakiye:", bakiye, "TL")

        else:
            print("Geçersiz tutar!")
            print("Yatırılacak miktar sıfırdan büyük olmalıdır.")

    elif secim == "3":
        print("Mevcut bakiye:", bakiye, "TL")

        tutar = float(input("Çekilecek tutar: "))

        if tutar <= 0:
            print("Geçersiz tutar!")
            print("Çekilecek miktar sıfırdan büyük olmalıdır.")

        elif tutar > bakiye:
            print("Yetersiz bakiye!")
            print("Mevcut bakiye:", bakiye, "TL")

        else:
            bakiye -= tutar
            print("Para çekme işlemi başarılı.")
            print("Güncel bakiye:", bakiye, "TL")

    else:
        print("Geçersiz işlem seçimi!")

else:
    print("Hatalı PIN kodu!")
    print("İşlem gerçekleştirilemedi.")

print("=== PROGRAM SONU ===")