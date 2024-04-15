tableau = []
n = int(input("Entrez le nombre de propositions : "))

for i in range(n):
    var = str(input(f"Entrez votre {i+1}è proposition : "))
    tableau.append(var)
    
# entête
tete = "\t".join(tableau)
print(tete)

# combinaison des propositions
for i in range(2**n):
    combinaison = [int(x) for x in bin(i)[2:].zfill(n)]
    ligne = "\t".join(map(str, combinaison))
    print(ligne)
    
# fonction OU
def OU(x, y):
    resultat = x or y
    return resultat

#  x
x = int(input(f"Entrez le numéro de la proposition pour x (de 1 à {n}) : ")) - 1
while x not in range(n) or tableau[x] not in ['0', '1']:
    print("La proposition entrée n'est pas valide. Veuillez entrer un numéro de proposition valide.")
    x = int(input(f"Entrez le numéro de la proposition pour x (de 1 à {n}) : ")) - 1

x = bool(int(tableau[x]))

#  y
y = int(input(f"Entrez le numéro de la proposition pour y (de 1 à {n}) : ")) - 1
while y not in range(n) or tableau[y] not in ['0', '1']:
    print("La proposition entrée n'est pas valide. Veuillez entrer un numéro de proposition valide.")
    y = int(input(f"Entrez le numéro de la proposition pour y (de 1 à {n}) : ")) - 1

y = bool(int(tableau[y]))

resultat = OU(x, y)
print("Le résultat de l'opération logique OR est :", resultat)

#la meme chose pour la fonction et
def ET(x, y):
    resultat2 = x and y
    return resultat2
#  x2
x2 = int(input(f"Entrez le numéro de la proposition pour x (de 1 à {n}) : ")) - 1
while x2 not in range(n) or tableau[x2] not in ['0', '1']:
    print("La proposition entrée n'est pas valide. Veuillez entrer un numéro de proposition valide.")
    x2 = int(input(f"Entrez le numéro de la proposition pour x (de 1 à {n}) : ")) - 1

x2 = bool(int(tableau[x2]))

#  y
y2 = int(input(f"Entrez le numéro de la proposition pour y (de 1 à {n}) : ")) - 1
while y not in range(n) or tableau[y2] not in ['0', '1']:
    print("La proposition entrée n'est pas valide. Veuillez entrer un numéro de proposition valide.")
    y2 = int(input(f"Entrez le numéro de la proposition pour y (de 1 à {n}) : ")) - 1

y2 = bool(int(tableau[y2]))

resultat = ET(x2, y2)
print("Le résultat de l'opération logique OR est :", resultat)    