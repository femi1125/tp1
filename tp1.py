n = int(input("Entrez un nombre entier  "))
fact = 1
i = 1

while i <= n:
    fact *= i
    i += 1

print("La factorielle de", n," est :", fact)

print("\nRésultat pour les nombres de 1 à 50 :")
num = 1
while num <= 50:
    if num % 5 == 0 :
        print(num,":Murielle ")
    elif num % 3 == 0 and num % 5 == 0:
        print(num,":BIBI Murielle")
    elif num % 3 == 0:
        print(num,":BIBI")
    else:
        print(num)
    num += 1

