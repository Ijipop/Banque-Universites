# 🎓 Système de Gestion Universitaire

Application de gestion des universités et facultés avec interface graphique PySide6 et base de données SQLAlchemy.

## 📋 Prérequis

- Python `3.9+`
- Windows/Linux/Mac

## 🚀 Installation et Lancement

### Option 1 : Installation Rapide (Recommandée)

```bash
# 1. Cloner ou télécharger le projet
# 2. Ouvrir un terminal dans le dossier du projet

# 3. Créer l'environnement virtuel
python -m venv env

# 4. Activer l'environnement virtuel
# Windows :
env\Scripts\activate
# Linux/Mac :
source env/bin/activate

# 5. Installer les dépendances
pip install -r requirements.txt

# 6. Lancer l'application
python main.py
```

### Option 2 : Installation Manuelle

```bash
# Installer les packages individuellement
pip install PySide6 SQLAlchemy
```

## 🎯 Utilisation

### Lancement de l'Application
```bash
# Avec l'environnement virtuel activé
python main.py

# Ou directement avec l'interpréteur de l'environnement
env\Scripts\python.exe main.py  # Windows
env/bin/python main.py          # Linux/Mac
```

### Fonctionnalités

- **📊 Gestion des Universités** : Ajouter, visualiser et supprimer des universités
- **🏛️ Gestion des Facultés** : Ajouter des facultés liées aux universités
- **🔗 Listes Dépendantes** : Sélection automatique des facultés selon l'université choisie
- **📈 Statistiques** : Visualisation des données de la base
- **🗑️ Suppression** : Suppression avec confirmation et cascade automatique

### Démonstration
```bash
# Lancer le script de démonstration
python demo.py
```

## 📁 Structure du Projet

```
université_gestion/
├── main.py              # Application principale
├── interface.py         # Interface utilisateur générée
├── interface.ui         # Fichier de design Qt
├── database.py          # Modèles et fonctions de base de données
├── demo.py              # Script de démonstration
├── requirements.txt     # Dépendances Python
├── env/                 # Environnement virtuel
└── universites_facultes.db  # Base de données SQLite
```

## 🛠️ Dépannage

### Erreur "Module not found"
```bash
# Vérifier que l'environnement virtuel est activé
# Windows : env\Scripts\activate
# Linux/Mac : source env/bin/activate

# Réinstaller les dépendances
pip install --force-reinstall -r requirements.txt
```

### Problème de base de données
```bash
# Supprimer la base existante pour recommencer
rm universites_facultes.db  # Linux/Mac
del universites_facultes.db  # Windows
```

## 📝 Notes

- La base de données SQLite est créée automatiquement au premier lancement
- Les données de démonstration sont ajoutées automatiquement
- L'application utilise des contraintes de clés étrangères pour maintenir l'intégrité des données


Initialement créé dans le cadre d'un cours de programmation

**Créé par Natacha Meyer & Jean-François Lefebvre**
