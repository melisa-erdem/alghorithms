
dizi = list(map(int, input("Bir dizi girin (aralarında boşluk bırakarak): ").split()))

frekanslar = {}

for eleman in dizi:
    if eleman in frekanslar:
        frekanslar[eleman] += 1
    else:
        frekanslar[eleman] = 1

print("Tekrar eden elemanlar ve sayıları:")
for eleman, frekans in frekanslar.items():
    if frekans > 1:
        print(f"Eleman: {eleman}, Tekrar Sayısı: {frekans}")
