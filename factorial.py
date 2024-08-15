
n = int(input("Faktöriyelini bulmak istediğiniz sayıyı girin\n"))
factorial = 1
 
if n >= 0:
    for i in range(1, n + 1):
        factorial *= i
    print(f"Girdiğiniz sayının faktöriyeli: {n}! = {factorial}")
else:
    print("Negatif sayıların faktöriyeli yok.")