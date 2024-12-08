i = 0
for de1 in range(1,7):
      for de2 in range(1,7):
         for de3 in range(1,7):
          for de4 in range(1,7):
                for de5 in range(1,7):
                    somme = de1 + de2 + de3 + de4 + de5
                    if somme == 20:
                        print(f"Combinaison : {de1}, {de2}, {de3}, {de4}, {de5}")
                        i += 1
print(f"Nombre total de façons d'obtenir 20 : {i}")
