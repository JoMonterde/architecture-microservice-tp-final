# Architecture micro-service - TP FINAL IRC - Groupe 1 : user-service 

## 📌 Rôle de chaque membre 
#### Répartition des rôles dans l’équipe
* Responsable documentation : Jodie et Morgane
* Developpeur principal Python : Alberto et Romain
* Responsable tests : ?

## 🗓️ Déroulé du projet 
#### Lundi 7 juillet 2025
#### 13h30 : Lancement du Projet 
- Lecture du projet 
- Choix des micro-services par groupes
- Choix des rôles dans le groupe 
#### 14h30 : Réflexion et Organisation
- Travail sur la structure des données JSON
- Extraction des routes API, leur fonctionnement et leurs retours
- Début de la dockerisation du service
- Échanges avec les autres Groupes :  
Groupe 3 - Demande : Récupérer tous les canaux associés à un utilisateur donné.  
Réponse : Proposition de récupérer tous les utilisateurs liés à un canal. Question sur la séparation des responsabilités entre les services et les limites. Après discussion, la récupération de tous les canaux associés à un utilisateur donné, relève de notre service.  
Groupe 2 - Demande : Une requête pour obtenir le dernier message horodaté d’un utilisateur.  
Réponse : Cette route devra être masquée, car elle ne doit pas être accessible publiquement.  
#### 15h30 : Lancement du Code et de la Documentation 
- Début de l'implémentation en Python
- Début de la rédaction de la documentation 
- Complesion d’un document partagé à l’ensemble des groupes regroupant : routes API, détails des requêtes, clé JWT 
#### 16h00 : Structuration du Projet 
- Début de la connexion Client/Serveur 
#### 17h00 : Fin de la journée

#### Mardi 8 juillet 2025
#### 8h30 : Remise dans le bain 
- Relecture du sujet
- Reprise du code 
- Recadrage de la documentation
- Demande du groupe 4 pour 10h : un conteneur viable pour commencer les tests
#### 9h36 : Youpiiii ça marche !
- /register est fonctionnel : Créer un compte utilisateur
#### 10h00 : Deadline !
- Rendu au groupe 4 d'un conteneur fonctionnel
#### 10h30 : Initiative de Romain 
TODO 
#### 11h00 : Demande du groupe 3 
- Demande : Un moyen de récupérer le pseudo.  
Réponse : Le JWT contient les informations. Explication de l’extraction des données dans la clé cryptée, et ajout les détails dans la documentation commune.
#### 11h10 : Youpiiii ça marche !
- /whois est fonctionnel : Infos publiques sur un utilisateur
#### 11h30 : Tests
- Listes des tests à faire
#### 12h00 : Pause dej
