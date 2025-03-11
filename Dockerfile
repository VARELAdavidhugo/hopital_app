# Utilisation de l'image officielle Python
FROM python:3.12

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier tous les fichiers de l'application dans le conteneur
COPY . /app

# Installer les dépendances
RUN pip install --no-cache-dir flask flask-mysqldb flask-cors

# Exposer le port 5000 pour Flask
EXPOSE 5000

# Commande pour exécuter l'application Flask
CMD ["python", "app.py"]
