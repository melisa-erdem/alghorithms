
sinav1 = float(input("Birinci sınav notunu girin: "))
sinav2 = float(input("İkinci sınav notunu girin: "))
sinav3 = float(input("Üçüncü sınav notunu girin: "))

ortalama = (sinav1 + sinav2 + sinav3) / 3

if ortalama >= 90:
    harf_notu = "AA"
elif ortalama >= 80:
    harf_notu = "BA"
elif ortalama >= 70:
    harf_notu = "BB"
elif ortalama >= 60:
    harf_notu = "CB"
elif ortalama >= 50:
    harf_notu = "CC"
else:
    harf_notu = "FF"

print(f"Ortalamanız: {ortalama:.2f} - Harf notunuz: {harf_notu}")
