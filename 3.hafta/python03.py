# ==========================================
# 1. IF YAPISI
# ==========================================

# if: Koşul doğruysa ilgili kod bloğu çalışır.
# Python'da kod blokları girintileme ile belirlenir.

yas = int(input("Yaşınızı giriniz: "))

if yas >= 18:
    print("18 yaşından büyüksünüz veya 18 yaşındasınız.")

print("Program devam ediyor.")


# ==========================================
# 2. IF - ELSE YAPISI
# ==========================================

# if: Koşul doğruysa çalışır.
# else: Koşul yanlışsa çalışır.

yas = int(input("Yaşınızı giriniz: "))

if yas >= 18:
    print("Reşitsiniz.")
else:
    print("Henüz reşit değilsiniz.")


# Tek - çift sayı kontrolü

sayi = int(input("Bir sayı giriniz: "))

if sayi % 2 == 0:
    print("Girdiğiniz sayı çifttir.")
else:
    print("Girdiğiniz sayı tektir.")


# ==========================================
# 3. IF - ELIF - ELSE YAPISI
# ==========================================

# Birden fazla koşulu kontrol etmek için kullanılır.
# Koşullar yukarıdan aşağıya kontrol edilir.
# İlk doğru koşulun bloğu çalışır.

not_ortalamasi = float(input("Not ortalamanızı giriniz: "))

if not_ortalamasi >= 85:
    print("Harf notunuz: AA")
elif not_ortalamasi >= 70:
    print("Harf notunuz: BB")
elif not_ortalamasi >= 50:
    print("Harf notunuz: CC")
else:
    print("Harf notunuz: FF")


# Pozitif - negatif - sıfır kontrolü

sayi = int(input("Bir sayı giriniz: "))

if sayi > 0:
    print("Pozitif sayı")
elif sayi < 0:
    print("Negatif sayı")
else:
    print("Sayı sıfırdır.")


# ==========================================
# 4. KOŞULLARDA AND OPERATÖRÜ
# ==========================================

# and: Her iki koşul da True olmalıdır.

yas = int(input("Yaşınızı giriniz: "))
ortalama = float(input("Ortalamanızı giriniz: "))

if yas >= 18 and ortalama >= 70:
    print("Başvuru şartlarını sağlıyorsunuz.")
else:
    print("Başvuru şartlarını sağlamıyorsunuz.")


# ==========================================
# 5. KOŞULLARDA OR OPERATÖRÜ
# ==========================================

# or: Koşullardan en az biri True olmalıdır.

ogrenci_mi = input("Öğrenci misiniz? (evet/hayır): ")
yas = int(input("Yaşınızı giriniz: "))

if ogrenci_mi == "evet" or yas < 18:
    print("İndirim hakkınız bulunmaktadır.")
else:
    print("İndirim hakkınız bulunmamaktadır.")


# ==========================================
# 6. KOŞULLARDA NOT OPERATÖRÜ
# ==========================================

# not: Koşulun mantıksal değerini tersine çevirir.

sistem_aktif = False

if not sistem_aktif:
    print("Sistem şu anda aktif değil.")
else:
    print("Sistem çalışıyor.")


# ==========================================
# 7. İÇ İÇE KOŞULLAR (NESTED IF)
# ==========================================

# Bir koşulun içerisinde başka bir koşul bulunabilir.

kullanici_adi = input("Kullanıcı adınızı giriniz: ")
sifre = input("Şifrenizi giriniz: ")

if kullanici_adi == "admin":
    if sifre == "1234":
        print("Giriş başarılı.")
    else:
        print("Şifre hatalı.")
else:
    print("Kullanıcı bulunamadı.")

# Not: Bu ornek yalnizca kosul mantigini gostermek icindir.
# Gercek sistemlerde sifreler kod icerisinde acik tutulmaz.


# ==========================================
# 9. KOSULLARIN SIRALAMASI
# ==========================================

# Kosullarin sirasi programin sonucunu etkiler.

puan = 90

# Hatali mantiksal siralama
if puan >= 50:
    print("Geçti")
elif puan >= 85:
    print("Pekiyi")

# Yukaridaki ornekte ikinci kosula ulasilmaz.
# Cunku 90 >= 50 kosulu zaten dogrudur.

# Dogru siralama
if puan >= 85:
    print("Pekiyi")
elif puan >= 50:
    print("Gecti")
else:
    print("Kaldi")
