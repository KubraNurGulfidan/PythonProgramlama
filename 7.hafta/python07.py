# Fonksiyon tanımlama

def selamla():
    print("Merhaba Python!")

# Fonksiyon çağırma

selamla()
selamla()
selamla()

# Parametre ve argüman
def selamla(isim):
    print("Merhaba", isim)

selamla("Ayşe")
selamla("Ali")
selamla("Mehmet")

selamla()

# Birden fazla parametre

def topla(a, b):
    print("Toplam:", a + b)

topla(10, 20)
topla(5, 8)

# Print return farkı

def topla2(a, b):
    return a + b

sonuc = topla2(10, 20)

print("Sonuç:", sonuc)
print("İki katı:", sonuc * 2)

def hesapla(a, b):
    toplam = a + b
    carpim = a * b

    return toplam, carpim

sonuc1, sonuc2 = hesapla(5, 3)

print("Toplam:", sonuc1)
print("Çarpım:", sonuc2)

# Varsayılan parametre

def kdv_hesapla(tutar, oran=0.20):
    return tutar * oran

print(kdv_hesapla(1000))
print(kdv_hesapla(1000, 0.10))

# Fonksiyonlarda koşul

def basari_kontrol(not_degeri):
    if not_degeri >= 50:
        return "Başarılı"
    else:
        return "Başarısız"

print(basari_kontrol(75))
print(basari_kontrol(40))

# Fonksiyonlarda döngüler

def sayilari_yazdir(n):
    for i in range(1, n + 1):
        print(i)

sayilari_yazdir(5)

# Fonksiyonlarda liste ve sözlükler

def ortalama_hesapla(notlar):
    toplam = 0

    for not_degeri in notlar:
        toplam += not_degeri

    return toplam / len(notlar)

notlar = [70, 80, 90, 60]

print("Ortalama:", ortalama_hesapla(notlar))

# Yerel ve global değişkenler

sayi = 10

def ornek():
    sayi = 20
    print("Fonksiyon içindeki:", sayi)

ornek()

print("Fonksiyon dışındaki:", sayi)

sayi = 10

def hesapla():
    #global sayi
    sayi = sayi + 5
    print(sayi)

hesapla()