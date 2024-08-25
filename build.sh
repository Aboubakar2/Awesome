#!/bin/bash

# Mise à jour de pip
python3 -m pip install --upgrade pip

# Installation des dépendances
python3 -m pip install -r requirements.txt

#appliquer les migrations
python3 manage.py makemigrations

python3 manage.py migrate

# Collecte des fichiers statiques
python3 manage.py collectstatic --noinput

# Vous pouvez ajouter d'autres commandes ici si nécessaire