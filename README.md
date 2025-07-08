# Architecture micro-service - TP FINAL IRC - Groupe 1 : user-service 
#### auteurs: Romain COURBAIZE, Jodie MONTERDE, Alberto MOUNGONDO, Morgane MICHEL

## 🎯 Objectif du projet 
Le User-Service est un micro-service central chargé de l’authentification et de la gestion des utilisateurs dans l’architecture IRC distribuée. Il gère les comptes utilisateurs, les statuts de connexion, les avatars, et les rôles globaux. Il est responsable de l’émission et de la vérification des jetons JWT, garantissant des accès sécurisés aux autres services. Entièrement stateless et dockerisé, il expose des endpoints HTTP en JSON, avec stockage en mémoire ou via MySQL selon l’avancement.

## 🚀 Instruction de lancement 
TODO

## Exemple d'appel
TODO

## 📦 Contenu du dépôt
### Documentation  
- `README.md` : Ce fichier
- `authors.md` : URL du dépôt et les membres du groupe 
- `group.md` : Rôle de chaque membre et déroulé du projet
- `DocumentationAPI.md` : Documentation de l'API avec toutes les routes (en parallèle avec Flasgger TODO)
### Code
- `Pipfile` : Déclaration des dépendances
- `Pipfile.lock` : Geler les versions exactes
- `requirements.txt` : Lister les dépendances Python
- `Dockerfile` : Image Docker du service
- `docker-compose.yml` : Orchestration multi-conteneurs
- `app.py` : Fichier serveur avec toutes les routes
- `user.py` : Fichier client
- `auth.py` : Configuration du JWT et du hashage 
- `config.py` : Struture du JWT 


