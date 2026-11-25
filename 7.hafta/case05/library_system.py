# CASE 05 - KUTUPHANE YONETIM SISTEMI

kitaplar = {
    "K101": {"ad": "Sefiller", "stok": 3, "oduncte": 0},
    "K102": {"ad": "Suç ve Ceza", "stok": 2, "oduncte": 0},
    "K103": {"ad": "Kürk Mantolu Madonna", "stok": 4, "oduncte": 0},
    "K104": {"ad": "Simyacı", "stok": 1, "oduncte": 0}
}


# 1. KITAPLARI LISTELEME
def kitaplari_listele(kitaplar):
    print("\n--- KITAP LISTESI ---")

    for kod, bilgi in kitaplar.items():
        print("Kitap kodu:", kod)
        print("Kitap adı:", bilgi["ad"])
        print("Mevcut stok:", bilgi["stok"])
        print("Ödünçte:", bilgi["oduncte"])
        print("--------------------")


# 2. KITAP ARAMA
def kitap_ara(kitaplar, kod):
    if kod in kitaplar:
        return kitaplar[kod]
    else:
        return None


# 3. KITAP EKLEME / STOK GUNCELLEME
def kitap_ekle(kitaplar):
    kod = input("Kitap kodu: ")

    if kod in kitaplar:
        print("Kitap zaten kayıtlı.")
        print("Kitap adı:", kitaplar[kod]["ad"])

        miktar = int(input("Eklenecek stok miktarı: "))

        if miktar > 0:
            kitaplar[kod]["stok"] += miktar
            print("Stok başarıyla güncellendi.")
            print("Güncel stok:", kitaplar[kod]["stok"])
        else:
            print("Stok miktarı pozitif olmalıdır.")

    else:
        ad = input("Kitap adı: ")
        miktar = int(input("Başlangıç stok miktarı: "))

        if miktar > 0:
            kitaplar[kod] = {
                "ad": ad,
                "stok": miktar,
                "oduncte": 0
            }
            print("Yeni kitap başarıyla eklendi.")
        else:
            print("Stok miktarı pozitif olmalıdır.")


# 4. KITAP ODUNC VERME
def kitap_odunc_ver(kitaplar):
    kod = input("Kitap kodu: ")

    if kod in kitaplar:
        if kitaplar[kod]["stok"] > 0:
            kitaplar[kod]["stok"] -= 1
            kitaplar[kod]["oduncte"] += 1

            print("Kitap:", kitaplar[kod]["ad"])
            print("Ödünç verme başarılı.")
            print("Kalan stok:", kitaplar[kod]["stok"])
        else:
            print("Bu kitabın stoğu bulunmuyor.")
    else:
        print("Kitap sistemde kayıtlı değil.")


# 5. KITAP IADE ETME
def kitap_iade_et(kitaplar):
    kod = input("Kitap kodu: ")

    if kod in kitaplar:
        if kitaplar[kod]["oduncte"] > 0:
            kitaplar[kod]["stok"] += 1
            kitaplar[kod]["oduncte"] -= 1

            print("Kitap:", kitaplar[kod]["ad"])
            print("İade başarılı.")
            print("Güncel stok:", kitaplar[kod]["stok"])
        else:
            print("Bu kitap için ödünç kaydı bulunmuyor.")
    else:
        print("Kitap sistemde kayıtlı değil.")


# ANA PROGRAM
while True:
    print("\n=== KÜTÜPHANE YÖNETİM SİSTEMİ ===")
    print("1 - Kitapları Listele")
    print("2 - Kitap Ara")
    print("3 - Kitap Ekle / Stok Güncelle")
    print("4 - Kitap Ödünç Ver")
    print("5 - Kitap İade Et")
    print("6 - Çıkış")

    secim = input("İşlem seçiniz: ")

    if secim == "1":
        kitaplari_listele(kitaplar)

    elif secim == "2":
        kod = input("Aranacak kitap kodu: ")
        sonuc = kitap_ara(kitaplar, kod)

        if sonuc != None:
            print("Kitap adı:", sonuc["ad"])
            print("Mevcut stok:", sonuc["stok"])
            print("Ödünçte:", sonuc["oduncte"])
        else:
            print("Kitap bulunamadı.")

    elif secim == "3":
        kitap_ekle(kitaplar)

    elif secim == "4":
        kitap_odunc_ver(kitaplar)

    elif secim == "5":
        kitap_iade_et(kitaplar)

    elif secim == "6":
        print("Program sonlandırılıyor.")
        break

    else:
        print("Geçersiz seçim!")
