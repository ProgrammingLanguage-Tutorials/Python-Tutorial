# 💡 Voici différents types de variables en Python :

nb1 = 7                                     # int → nombre entier
nb2 = 1.3                                   # float → dicimaux
ch = "la première vidéo sur les variables"  # str → chaîne de caractères
L = [8, 9, 12, 0]                           # list → liste de valeurs
monboolean = False                          # bool → valeur booléenne (vrai ou faux)

# 🎯 On peut aussi affecter plusieurs variables en une seule ligne :
nb3, nb4, nb5 = 8, 9, 4

# ➕ Opérations entre variables :
resultatAddition = nb3 + nb4 + nb5

print("Hello world : ", int(monboolean))
# print("Résultat de l'addition :", resultatAddition)

"""
Tout les types d'opérateur
a = 10
b = 3

print(a + b)  # Addition => 13
print(a - b)  # Soustraction => 7
print(a * b)  # Multiplication => 30
print(a / b)  # Division flottante => 3.333...
print(a // b) # Division entière => 3
print(a % b)  # Modulo => 1
print(a ** b) # Puissance => 1000

"""

# 📥 Demander une valeur à l'utilisateur :
mot = input("Saisie un mot : ")
nb6 = int(input("Saisir un nombres : "))
print("Tu as saisi :", nb6, ":" ,mot)
print("Le type de cette variable est :", type(nb6))  # Affiche <class 'int'>

# 🧪 Exemple : afficher le type d'une autre variable avec la fonction type
print(type(monboolean))