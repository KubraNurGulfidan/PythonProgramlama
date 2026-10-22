# ==========================================
# 1. Kullanıcıdan veri alma ve veri tiplerini gösterme
# ==========================================
isim = input("Lütfen isminizi giriniz: ")
print("Merhaba, " + isim + "! Hoş geldiniz.")

yas = input("Lütfen yaşınızı giriniz: ")
print(yas)
print(type(yas))


# ==========================================
# 2. Type casting
# ==========================================
yas = int(yas)
boy= float(input("Lütfen boyunuzu metre cinsinden giriniz: "))
print(yas)
print(type(yas))
print(boy)
print(type(boy))


# ==========================================
# 3. Matematiksel işlemler
# ==========================================
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)


# ==========================================
# 4. Operator önceliği
# ==========================================
"""
1. Parantez ()
2. Üs alma **
3. Çarpma ve bölme * /
4. Toplama ve çıkarma + -
"""
print(2 + 3 * 4)
print((2 + 3) * 4)


# ==========================================
# 5. Karşılaştırma operatörleri
# ==========================================
a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)


# ==========================================
# 6. Mantıksal operatörler
# ==========================================
yas = 20
ortalama = 70

print(yas >= 18 and ortalama >= 50)
print(yas >= 18 or ortalama >= 80)
print(not yas >= 18)


# ==========================================
# 7. Atama operatörleri
# ==========================================
sayi = 10

sayi += 5
print(sayi)

sayi -= 3
print(sayi)

sayi *= 2
print(sayi)

sayi /= 4
print(sayi)