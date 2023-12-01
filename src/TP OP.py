import os

def lister_fichiers():
    # Récupérer la liste des fichiers/dossiers dans le répertoire actuel
    fichiers = os.listdir()

    # Afficher chaque fichier/dossier
    for fichier in fichiers:
        print(fichier)

# Appeler la fonction pour lister les fichiers dans le répertoire actuel
lister_fichiers()
