
metin = input("Bir metin girin: ")

harf_frekansi = {}

for harf in metin:
    if harf.isalpha(): 
        harf = harf.lower()  
        if harf in harf_frekansi:
            harf_frekansi[harf] += 1
        else:
            harf_frekansi[harf] = 1
for harf, frekans in harf_frekansi.items():
    print(f"{harf}: {frekans}")
