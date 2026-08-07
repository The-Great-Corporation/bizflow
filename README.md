# bizflow
Projet créé dans le cadre de The Great Bootcamp
## Description
bizflow est une application en ligne de commande permettant à un petit commerce de gérer son stock de produits

## Outils techniques
_Langage: Python
_Stockage: fichier JSON
_Interface: CLI
_Tests: Pytest
_Qualite de code: Black, Ruff

## Fonctionnalités du projet
- [x] Ajouter et lister des catégories
- [x] Ajouter et lister des fournisseurs
- [x] Ajouter un produit
- [x] Enregistrer une entrée et une sortie de stock
- [x] Lister les produits disponibles
- [x] Calculer la valeur totale du stock
- [x] Afficher les produits en rupture
- [x] Sauvegarde et chargement des données

## Architecture du projet
bizflow/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── categorie.py
│   │   ├── fournisseur.py
│   │   ├── mouvement_stock.py
│   │   └── produit.py
│   └── services/
│       ├── __init__.py
│       └── gestionnaire_stock.py
├── tests/
│   ├── __init__.py
│   ├── test_gestionnaire_stock.py
│   └── test_produit.py
├── donnees/
├── documentation/
├── .gitignore
├── README.md
├── requirements.txt

## Installation
\`\`\`bash
git clone <https://github.com/The-Great-Corporation/bizflow.git>
cd bizflow
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
\`\`\`

## Utilisation

Lancer l'application :
\`\`\`bash
python -m app.main
\`\`\`

Un menu interactif s'affiche avec les options suivantes :
1. Ajouter un produit
2. Lister les produits
3. Enregistrer un mouvement de stock (entrée ou sortie)
4. Voir les produits en alerte de stock
5. Sauvegarder et quitter

## Auteur
ANANI Dede Louise Sylvana