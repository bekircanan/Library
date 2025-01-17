# projet_G2S3A_Senelet_Canan

## Description

Ce projet est une application de recherche de livres qui permet aux utilisateurs de rechercher des livres dans une bibliothèque, de voir les détails des livres et de suivre les livres visités. L'application est construite en utilisant Python et Tkinter pour l'interface graphique.

## Fonctionnalités

- Importer des livres à partir d'un fichier CSV dans une liste chaînée.
- Rechercher des livres par titre, auteur, langue, style ou genre.
- Afficher les résultats de recherche dans un tableau.
- Naviguer dans l'historique des recherches.
- Voir les détails des livres visités et leur historique de recherche associé.

## Installation

1. Cloner le dépôt :

```Python
git clone https://forge.univ-lyon1.fr/p2310628/projet_g2s3a_senelet_canan.git
cd projet_g2s3a_senelet_canan
```

1. Assurez-vous d'avoir Python installé (version 3.6 ou supérieure).
2. Installer les dépendances requises :

```Python
pip install tk
```

## Utilisation

1. Exécuter l'application :

```Python
python projet/Main.py
```

2. Utiliser la barre de recherche pour entrer des termes de recherche et sélectionner la catégorie de recherche (Titre, Auteur, Langue, Style, Genre).

3. Cliquer sur "Rechercher" pour afficher les résultats de recherche dans le tableau.

4. Double-cliquer sur un livre dans les résultats de recherche pour l'ajouter à la liste des livres visités.

5. Double-cliquer sur un livre dans la liste des livres visités pour voir ses détails et l'historique de recherche associé.

6. Utiliser les boutons "Retour" et "Avancer" pour naviguer dans l'historique des recherches.

## Structure du projet

- projet
  - __pycache__/: Fichiers Python compilés.
    - livre.csv: Fichier CSV contenant la liste des livres.
    - Main.py: Fichier principal de l'application.
    - TD2.py: Contient les implémentations de la liste chaînée et de la pile.
- README.md: Documentation du projet.

## Auteurs

- Senelet
- Canan
