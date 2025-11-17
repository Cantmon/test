print("Yapmak istedğiniz işlemi seçniz (1/2/3/4)")
print("1. Çarpma")
print("2. Bölme")
print("3. Toplama")
print("4. Çıkarma")
secim = int(input("Seçiminiz (1/2/3/4): "))
if secim in (1, 2, 3, 4):
    num1 = float(input("Birinci sayıyı girin: "))
    num2 = float(input("İkinci sayıyı girin: "))
    if secim == 1:
        print(num1, "*", num2, "=", num1 * num2)
    elif secim == 2:
        print(num1, "/", num2, "=", num1 / num2)
    elif secim == 3:
        print(num1, "+", num2, "=", num1 + num2)
    elif secim == 4:
        print(num1, "-", num2, "=", num1 - num2)
else:
    print("Geçersiz giriş")