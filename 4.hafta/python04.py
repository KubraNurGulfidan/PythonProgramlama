# ==========================================
# 1. DÖNGÜLERE GİRİŞ
# ==========================================

# Döngüler, belirli işlemleri tekrar tekrar gerçekleştirmek için kullanılır.

# Döngü kullanmadan:
print("Merhaba")
print("Merhaba")
print("Merhaba")

# Döngü kullanarak:
for i in range(3):
    print("Merhaba")


# ==========================================
# 2. WHILE DÖNGÜSÜ
# ==========================================

# while döngüsü, belirtilen koşul True olduğu sürece çalışmaya devam eder.

sayac = 1

while sayac <= 5:
    print("Sayaç:", sayac)
    sayac += 1

print("Döngü sona erdi.")


# ==========================================
# 3. WHILE DÖNGÜSÜ - KULLANICI GİRİŞİ
# ==========================================

# Kullanıcı doğru şifreyi girene kadar program tekrar şifre ister.

sifre = ""

while sifre != "1234":
    sifre = input("Şifrenizi giriniz: ")

    if sifre != "1234":
        print("Hatalı şifre, tekrar deneyiniz.")

print("Giriş başarılı!")


# ==========================================
# 4. FOR DÖNGÜSÜ
# ==========================================

# for döngüsü, bir koleksiyonun veya sayı dizisinin elemanları üzerinde dolaşır.

# range(5) -> 0, 1, 2, 3, 4

for i in range(5):
    print(i)

# 1'den 10'a kadar sayıları yazdırma

for i in range(1, 11):
    print(i)


# ==========================================
# 5. RANGE() FONKSİYONU
# ==========================================

# range(bitis) -> 0'dan başlar, bitiş dahil değildir.

for i in range(5):
    print(i)

# range(baslangic, bitis) -> Başlangıç dahil, bitiş dahil değildir.

for i in range(2, 8):
    print(i)

# range(baslangic, bitis, adim)

for i in range(0, 11, 2):
    print(i)

# Geriye doğru sayma

for i in range(10, 0, -1):
    print(i)


# ==========================================
# 6. FOR VE WHILE KARŞILAŞTIRMASI
# ==========================================

# 1'den 5'e kadar sayıları for ile yazdırma

for i in range(1, 6):
    print(i)

# Aynı işlemi while ile yapma

sayac = 1

while sayac <= 5:
    print(sayac)
    sayac += 1


# ==========================================
# 7. BREAK İFADESİ
# ==========================================

# break, döngüyü tamamen sonlandırır.

for i in range(1, 11):

    if i == 6:
        break

    print(i)

print("Döngü bitti.")


# ==========================================
# 8. CONTINUE İFADESİ
# ==========================================

# continue, döngünün mevcut tekrarındaki kalan işlemleri atlar. Döngü sonraki tekrardan devam eder.

for i in range(1, 11):

    if i == 6:
        continue

    print(i)


# ==========================================
# 9. DÖNGÜLER VE KOŞUL İFADELERİ
# ==========================================

# 1'den 20'ye kadar çift sayıları yazdırma

for sayi in range(1, 21):

    if sayi % 2 == 0:
        print(sayi)


# 1'den 20'ye kadar tek sayıları yazdırma

for sayi in range(1, 21):

    if sayi % 2 != 0:
        print(sayi)


# ==========================================
# 10. DÖNGÜ İLE TOPLAMA İŞLEMİ
# ==========================================

# 1'den 100'e kadar sayıların toplamı

toplam = 0

for i in range(1, 101):
    toplam += i

print("Toplam:", toplam)


# ==========================================
# 11. KULLANICIDAN TEKRARLI VERİ ALMA
# ==========================================

# Kullanıcıdan 5 sayı alınır.
# Sayıların toplamı ve ortalaması hesaplanır.

toplam = 0

for i in range(5):

    sayi = float(input("Bir sayı giriniz: "))
    toplam += sayi

ortalama = toplam / 5

print("Toplam:", toplam)
print("Ortalama:", ortalama)


# ==========================================
# 12. İÇ İÇE DÖNGÜLER (NESTED LOOPS)
# ==========================================

# Bir döngünün içerisinde başka bir
# döngü bulunabilir.

for i in range(1, 4):

    for j in range(1, 4):
        print("i =", i, "j =", j)


# ==========================================
# 13. İÇ İÇE DÖNGÜLER - YILDIZ DESENİ
# ==========================================

# print() varsayılan olarak satır sonu ekler.
# end="" aynı satırda yazmaya devam eder.

for i in range(1, 6):

    for j in range(i):
        print("*", end="")

    print()

"""
Çıktı:
*
**
***
****
*****
"""

# ==========================================
# 14. WHILE TRUE VE BREAK
# ==========================================

# while True sonsuz döngü oluşturur.
# Döngü break ile sonlandırılabilir.

while True:

    secim = input("Çıkmak için q giriniz: ")

    if secim == "q":
        print("Programdan çıkılıyor.")
        break

    print("Program çalışmaya devam ediyor.")


# ==========================================
# 15. BİRLİKTE UYGULAMA
# SAYI TAHMİN OYUNU
# ==========================================

gizli_sayi = 7
tahmin = 0
deneme_sayisi = 0

print("=== SAYI TAHMİN OYUNU ===")

while tahmin != gizli_sayi:

    tahmin = int(input("1-10 arasında sayı tahmin ediniz: "))
    deneme_sayisi += 1

    if tahmin < gizli_sayi:
        print("Daha büyük bir sayı giriniz.")

    elif tahmin > gizli_sayi:
        print("Daha küçük bir sayı giriniz.")

    else:
        print("Tebrikler! Doğru tahmin.")

print("Toplam deneme sayısı:", deneme_sayisi)
print("=== OYUN BİTTİ ===")