
n = int(input("Dizi boyutunu girin: "))
dizi = []
for i in range(n):
    eleman = int(input(f"{i+1}. elemanı girin: "))
    dizi.append(eleman)
toplam = sum(dizi)

# Bubble Sort algoritması
for i in range(n):
    for j in range(0, n-i-1):
        if dizi[j] > dizi[j+1]:
            dizi[j], dizi[j+1] = dizi[j+1], dizi[j]
print("Sıralı dizi:", dizi)