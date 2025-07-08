# Architecture micro-service - TP FINAL IRC - Groupe 1 : user-service 

## 📌 Rôle de chaque membre 
#### Répartition des rôles dans l’équipe
* Responsable documentation : Jodie et Morgane
* Developpeur principal Python : Alberto et Romain
* Responsable tests : Jodie, Alberto, Romain et Morgane

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
Réponse : Proposition de récupérer tous les utilisateurs liés à un canal. Question de la séparation des responsabilités entre les services et les limites. Après discussion, la récupération de tous les canaux associés à un utilisateur donné, relève de notre service.  
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
- Description de problèmes rencontrés
  - Lorsque l'on change de mot de passe est changé, le token précédemment émis devrait être invalidé.
  - La gestion des status aurait pu être gérée par le token (online/offline)
- Solution trouvée : s'apparente à l'utilisation d'une session
  - Stocker le token dans la base de données permettrait de pouvoir comparer le token envoyé par l'utilisateur et le dernier token émit par le serveur.
  - Stocker le token dans la base de données permettrait de connaître l'état de connexion à l'instant T. Un token en base de données et valide (non expiré) indiquerait que l'utilisateur est connecté, sinon déconnecté.
- Solution retenue : 
  - Nous avons décidé de ne pas stocker le token en base de données. Nous avons par contre stocké la date de dernière émission en base de données ce qui nous permet de connaître le status.  
Dans le cas d'un changement de mot de passe, il n'y aura pas de problème car le serveur pourra comparer l'ancienne date d'expiration avec celle en base. Dès le changement d'un mot de passe, la date sera mise à jour.  
#### 11h00 : Demande du groupe 3 
- Demande : Un moyen de récupérer le pseudo.  
Réponse : Le JWT contient les informations. Explication de l’extraction des données dans la clé cryptée, et ajout les détails dans la documentation commune.
#### 11h10 : Youpiiii ça marche !
- /whois est fonctionnel : Infos publiques sur un utilisateur
#### 11h30 : Tests
- Listes des tests à faire
#### 12h00 : Pause dej
#### 13h30 : Dernière ligne droite 
- /login est fonctionnel : Authentifier et retourner un JWT
- /ison est fonctionnel : Liste des utilisateurs actuellement connectés
- Lastseen est fonctionnel
- Création de Flasgger
#### 16h00 : Enfin fini
- Rendu du projet 
