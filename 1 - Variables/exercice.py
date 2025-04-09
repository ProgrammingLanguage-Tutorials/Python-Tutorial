"""
Demander a l'utilisateur plusieurs informations :
- Nom
- Prénom
- Age
Et afficher ses informations (à l'aide de print)
"""

nom = input("Quel est votre nom ? ")
prenom = input("Quel est votre prenom ? ")
age = int(input("Quel est votre age ? "))

print(f"Je m'appelle {prenom} {nom} et j'ai {age} age")