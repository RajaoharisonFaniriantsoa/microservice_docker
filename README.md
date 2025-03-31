RAJAOHARISON Faniriantsoa maminiaina 
classe:ARSB
Numero:67
# Architecture Microservices avec Docker

Un exemple complet d'architecture microservices combinant :
- Une application web Flask
- Une base de données PostgreSQL
- Un service de traitement de données Python (pandas/scikit-learn)

## 🚀 Fonctionnalités

- **Application Web** : Affiche des données depuis la base de données
- **Service de données** : Génère des données synthétiques et calcule des statistiques
- **Base de données** : PostgreSQL avec persistance des données
- **Orchestration** : Docker Compose pour gérer les services

## 📦 Structure du projet
microservice/
├── web-app/ # Application Flask
├── data-service/ # Traitement de données
├── db-init/ # Scripts SQL d'initialisation
├── docker-compose.yml # Configuration Docker
├── .env # Variables d'environnement
└── README.md

Démarrer les services 
->docker-compose up --build

Accéder à l'application
->[loalhost:5000](http://localhost:5000)

🌟 Services
1. Application Web (Flask)

    Port : 5000

    Fonction : Affiche les données de la base de données

    Technos : Python, Flask, PostgreSQL

2. Service de Traitement

    Fonction :

        Génère des données synthétiques

        Calcule des statistiques

        Stocke les résultats en base

    Technos : pandas, scikit-learn

3. Base de Données

    Image : postgres:13-alpine

    Port : 5432

    Persistance : Volume Docker

🔧 Configuration

Modifiez le fichier .env pour changer :

    Identifiants de la base de données

    Paramètres des services

📊 Exemple de Données

Le service génère automatiquement :

    100 échantillons de données synthétiques

    2 features et 1 label par échantillon

    Statistiques descriptives (moyenne, écart-type...)
