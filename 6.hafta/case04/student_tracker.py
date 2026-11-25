ogrenciler = []
notlar = {}
dersler = set()

ders_kodlari = ("PYT101", "MAT101", "ALG101")
ders_isimleri = ("Python", "Matematik", "Algoritma")

basari_siniri = 50

for i in range(5):

    while True:
        isim = input("Öğrenci adını giriniz: ")

        if isim == "":
            print("Öğrenci adı boş olamaz.")

        elif isim in ogrenciler:
            print("Bu öğrenci zaten kayıtlı.")

        else:
            ogrenciler.append(isim)
            break

    while True:
        not_degeri = float(input("Python notunu giriniz: "))

        if 0 <= not_degeri <= 100:
            notlar[isim] = not_degeri
            break

        else:
            print("Not 0 ile 100 arasında olmalıdır.")


print("\n=== DERS BİLGİLERİ ===")

for i in range(len(ders_kodlari)):
    print(ders_kodlari[i], "-", ders_isimleri[i])


for i in range(5):

    ders_adi = input("Ders adını giriniz: ")

    dersler.add(ders_adi)


while True:

    print("\n=== ÖĞRENCİ NOT TAKİP SİSTEMİ ===")

    print("1 - Öğrencileri Listele")
    print("2 - Notları Görüntüle")
    print("3 - Sınıf Ortalamasını Göster")
    print("4 - Başarılı / Başarısız Öğrenciler")
    print("5 - Dersleri Listele")
    print("6 - Çıkış")

    secim = input("İşlem seçiniz: ")

    if secim == "1":

        print("\n=== ÖĞRENCİLER ===")

        for isim in ogrenciler:
            print(isim)

    elif secim == "2":

        print("\n=== NOTLAR ===")

        for isim, not_degeri in notlar.items():
            print(isim, ":", not_degeri)

    elif secim == "3":

        toplam = 0

        for not_degeri in notlar.values():
            toplam += not_degeri

        ortalama = toplam / len(notlar)

        print("Sınıf ortalaması:", ortalama)
        print("En yüksek not:", max(notlar.values()))
        print("En düşük not:", min(notlar.values()))

    elif secim == "4":

        print("\n=== BAŞARILI ÖĞRENCİLER ===")

        for isim, not_degeri in notlar.items():

            if not_degeri >= basari_siniri:
                print(isim, "-", not_degeri)

        print("\n=== BAŞARISIZ ÖĞRENCİLER ===")

        for isim, not_degeri in notlar.items():

            if not_degeri < basari_siniri:
                print(isim, "-", not_degeri)

    elif secim == "5":

        print("\n=== DERS KODLARI ===")

        for i in range(len(ders_kodlari)):
            print(ders_kodlari[i], "-", ders_isimleri[i])

        print("\n=== BENZERSİZ DERSLER ===")

        for ders in dersler:
            print(ders)

    elif secim == "6":

        print("Programdan çıkılıyor.")
        break

    else:
        print("Geçersiz işlem seçimi!")


print("=== PROGRAM SONU ===")
