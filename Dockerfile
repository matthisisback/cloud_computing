# Dockerfile

# Étape 1 : base image officielle légère avec Python
FROM python:3.12-slim

# Étape 2 : répertoire de travail dans le conteneur
WORKDIR /app

# Étape 3 : copier les fichiers nécessaires
COPY src/ ./src
COPY data/ ./data
COPY requirements.txt .

# Étape 4 : installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Étape 5 : exposer le port Flask
EXPOSE 5000

# Étape 6 : lancer l'app Flask
CMD ["python", "src/app.py"]
