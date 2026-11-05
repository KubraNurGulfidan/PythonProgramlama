# ==========================================
# 1. VERİ YAPILARINA GİRİŞ
# ==========================================

# Birden fazla öğrencinin notunu ayrı değişkenlerde tutmak
not1 = 75
not2 = 80
not3 = 90

# Aynı bilgileri tek bir listede saklamak
notlar = [75, 80, 90]

print(notlar)
print(type(notlar))


# ==========================================
# 2. LİSTELER (LIST)
# ==========================================

# Liste, birden fazla veriyi tek bir değişkende saklamamızı sağlayan veri yapısıdır.
# Sıralıdırlar, değiştirilebilirler ve aynı elemandan birden fazla içerebilirler.
# Listeler köşeli parantezlerle [] oluşturulur. Elemanlar virgülle ayrılır. 
# Bir listenin içinde farklı veri tipleri de bulunabilir.

meyveler = ["elma", "armut", "muz", "elma"]

print(meyveler)
print(len(meyveler))

# İndeksleme: İlk elemanın indeksi 0'dır.
print(meyveler[0])
print(meyveler[1])

# Liste dilimleme (slicing)
# Başlangıç indeksi dahildir ancak bitiş indeksi dahil değildir.
print(meyveler[1:3])
print(meyveler[:2])
print(meyveler[2:])

# Eleman değiştirme
meyveler[1] = "çilek"
print(meyveler)

# Eleman ekleme


meyveler.append("kiraz") # append() sona ekler
meyveler.insert(1, "portakal") # insert() belirli bir konuma ekler
print(meyveler)

# Eleman silme
meyveler.remove("muz") # remove() verilen değeri siler
silinen = meyveler.pop() # pop() belirtilen indeksteki elemanı siler. İndeks verilmezse son elemanı çıkarır.
print("Silinen:", silinen)
print(meyveler)


# ==========================================
# 3. LİSTELER VE DÖNGÜLER
# ==========================================

notlar = [70, 85, 60, 95, 80]

for not_degeri in notlar:
    print(not_degeri)

# Toplam ve ortalama hesaplama
toplam = 0

for not_degeri in notlar:
    toplam += not_degeri

ortalama = toplam / len(notlar)

print("Toplam:", toplam)
print("Ortalama:", ortalama)

# Hazır fonksiyonlar
print("En yüksek:", max(notlar))
print("En düşük:", min(notlar))
print("Toplam:", sum(notlar))


# ==========================================
# 4. LİSTELERDE ARAMA VE SIRALAMA
# ==========================================

sayilar = [40, 10, 30, 20, 50]

if 30 in sayilar:
    print("30 listede bulunuyor.")

sayilar.sort()
print("Artan sıralama:", sayilar)

sayilar.sort(reverse=True)
print("Azalan sıralama:", sayilar)

print("30'un indeksi:", sayilar.index(30))
print("Eleman sayısı:", len(sayilar))


# ==========================================
# 5. DEMETLER (TUPLE)
# ==========================================

# Listeye çok benzer; birden fazla veriyi sıralı şekilde saklamamızı sağlar.
# Ancak liste ile tuple arasındaki en önemli fark şudur: Liste değiştirilebilir, tuple ise değiştirilemez.
# Tuple'lar genellikle normal parantezlerle () gösterilir.

koordinat = (10, 20)
print(koordinat)
print(type(koordinat))

print(koordinat[0])
print(koordinat[1])

# koordinat[0] = 50
# Bu satır TypeError oluşturur.

# Tek elemanlı tuple
tek_eleman = (5,)
print(type(tek_eleman))

# Tuple unpacking
x, y = koordinat
print("X:", x)
print("Y:", y)

# Tuple üzerinde döngü
renkler = ("kırmızı", "mavi", "yeşil")

for renk in renkler:
    print(renk)


# ==========================================
# 6. SÖZLÜKLER (DICTIONARY)
# ==========================================

# Sözlükler anahtar-değer (key-value) çiftleri tutar.

ogrenci = {
    "ad": "Ayşe",
    "yas": 20,
    "bolum": "Bilgisayar Programcılığı",
    "ortalama": 85
}

print(ogrenci)
print(type(ogrenci))

# Anahtar kullanarak erişim
print(ogrenci["ad"])
print(ogrenci["ortalama"])

# get() ile erişim
print(ogrenci.get("yas"))

# Değer güncelleme
ogrenci["ortalama"] = 90

# Yeni bilgi ekleme
ogrenci["sinif"] = 1

print(ogrenci)

# Eleman silme
ogrenci.pop("yas")
print(ogrenci)


# ==========================================
# 7. SÖZLÜKLER VE DÖNGÜLER
# ==========================================

notlar = {
    "Ali": 75,
    "Ayşe": 90,
    "Mehmet": 65
}

# Anahtarlar
for isim in notlar:
    print(isim)

# Anahtar ve değerler
for isim, not_degeri in notlar.items():
    print(isim, ":", not_degeri)

# Anahtarlar ve değerler
print(notlar.keys())
print(notlar.values())

# Belirli bir anahtarı kontrol etme
if "Ayşe" in notlar:
    print("Ayşe'nin notu:", notlar["Ayşe"])


# ==========================================
# 8. KÜMELER (SET)
# ==========================================

# Set, Türkçede küme olarak adlandırılır. Matematikte gördüğümüz kümelere benzer.
# Kümeler tekrar eden elemanları saklamaz. 
# Kümeler sıralı değildir, indeksleme desteklenmez.

sayilar = {1, 2, 3, 3, 4, 4, 5}

print(sayilar)
print(type(sayilar))

# Eleman ekleme ve çıkarma
sayilar.add(6)
sayilar.discard(2)

print(sayilar)

# Listeyi kümeye dönüştürme
liste = [1, 2, 2, 3, 3, 4]
benzersiz = set(liste)

print(benzersiz)


# ==========================================
# 9. KÜME İŞLEMLERİ
# ==========================================

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Birleşim
print("Birleşim:", A | B)

# Kesişim
print("Kesişim:", A & B)

# Fark
print("A - B:", A - B)

# Simetrik fark
print("Simetrik fark:", A ^ B)


# ==========================================
# 10. VERİ YAPILARINI BİRLİKTE KULLANMA
# ==========================================

# Öğrenci isimlerini listede tutma
isimler = ["Ali", "Ayşe", "Mehmet"]

# Notları sözlükte tutma
notlar = {
    "Ali": 75,
    "Ayşe": 90,
    "Mehmet": 65
}

# Ders kodları tuple olarak saklanır
ders_kodlari = ("PYT101", "MAT101")

# Tekrar etmeyen ders isimleri
dersler = {"Python", "Matematik", "Python"}

print("Öğrenciler:", isimler)
print("Ders kodları:", ders_kodlari)
print("Dersler:", dersler)

for isim in isimler:
    print(isim, "- Not:", notlar[isim])

    if notlar[isim] >= 50:
        print("Başarılı")
    else:
        print("Başarısız")