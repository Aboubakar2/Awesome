#!/bin/bash

# Mise à jour de pip
python3.12 -m pip install --upgrade pip

# Installation des dépendances
pip install -r requirements.txt

# Collecte des fichiers statiques
python manage.py collectstatic --noinput

# Vous pouvez ajouter d'autres commandes ici si nécessaire