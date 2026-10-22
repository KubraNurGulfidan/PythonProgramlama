isim = input("adınızı giriniz: " )

urun1_adi =input(("1.ürünün adını giriniz: "))
urun1_fiyat = float(input("1.ürünün fiyatini giriniz: "))
urun1_adet = int(input("1.ürünün adetini giriniz: "))

urun2_adi = input(("2.ürünün adını giriniz: "))
urun2_fiyat = float(input("2.ürünün fiyatini giriniz: "))
urun2_adet = int(input("2.ürünün adetini giriniz: "))

urun3_adi = input(("3.ürünün adını giriniz: "))
urun3_fiyat = float(input("3.ürünün fiyatini giriniz: "))
urun3_adet = int(input("3.ürünün adetini giriniz: "))

urun_tutari1 = urun1_fiyat * urun1_adet
urun_tutari2 = urun2_fiyat * urun2_adet
urun_tutari3 = urun3_fiyat * urun3_adet

aratoplam = urun_tutari1 + urun_tutari2 + urun_tutari3

#kdv %20
kdv = aratoplam * 0.20
geneltoplam = aratoplam + kdv
toplam_adet = urun1_adet + urun2_adet + urun3_adet

#kotroller
kontrol1 = aratoplam >= 1000
kontrol2 = toplam_adet >= 5
kontrol3 = kontrol1 and kontrol2

print("\n=== AKILLI ALIŞVERİŞ FATURASI ===\n")
print("müşteri adı " + isim)
print(urun1_adi + ": " + str(urun_tutari1) + " TL")
print(urun2_adi + ": " + str(urun_tutari2) + " TL")
print(urun3_adi + ": " + str(urun_tutari3) + " TL")

print("Ara toplam: " + str( aratoplam))
print("KDV (%20): " + str(kdv))
print("Genel toplam: " + str(geneltoplam))

print("\n=== FATURA SONU ===\n")

print("Ara toplam 1000 TL veya üzerinde mi? " + str(kontrol1))
print("Toplam ürün adedi en az 5 mi? " + str(kontrol2))
print("Her iki koşul da sağlanıyor mu? " + str(kontrol3))
