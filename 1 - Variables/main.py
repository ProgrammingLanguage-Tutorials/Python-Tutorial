# 💡 Voici différents types de variables en Python :

nb1 = 7                  # int → nombre entier
nb2 = 1.3                # float → nombre à virgule
ch = "la première vidéo sur les variables"  # str → chaîne de caractères
L = [8, 9, 12, 7]        # list → liste de valeurs
monboolean = True        # bool → valeur booléenne (vrai ou faux)

# 🎯 On peut aussi affecter plusieurs variables en une seule ligne :
nb3, nb4, nb5 = 8, 9, 4

# ➕ Opérations entre variables :
resultatAddition = nb3 + nb4 + nb5
print("Résultat de l'addition :", resultatAddition)

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
nb6 = int(input("Saisir un nombre : "))
print("Tu as saisi :", nb6)
print("Le type de cette variable est :", type(nb6))  # Affiche <class 'int'>

# 🧪 Exemple : afficher le type d'une autre variable avec la fonction type
print(type(monboolean))