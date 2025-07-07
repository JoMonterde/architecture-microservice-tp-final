# Architecture micro-service : TP FINAL - IRC
#### auteurs: Romain COURBAIZE, Jodie MONTERDE, Alberto MOUNGONDO, Morgane MICHEL


## Premiers points : Gestion des comptes

* Implémenter la route POST /register : création de compte (pseudo, mot de passe hashé, email) :  
POST /register body {  
    "pseudo": "Morgane",  
    "email": "morgane@gmail.com",  
    "pwd": "H4iWy"  
}  
reponse : 201 Created : Le compte a été créé avec succès

* Implémenter la route POST /login : authentification et génération d’un JWT :  
POST /login body {  
    "email": "morgane@gmail.com",  
    "pwd": "H4iWy"  
}
reponse : 200 OK  
header : {  
    "jwt" : "Authorization: Bearer <le_token>"  
}  

* Utiliser un secret JWT dans les variables d’environnement  

* Durée d’expiration du token configurable :  
Choix de 2 heures  

## Un peu plus en détail : Informations sur les utilisateurs

* GET /whois/<pseudo> : informations publiques (status, canaux, rôles)  
GET /whois/<pseudo>  
reponse : 200 OK  
header : {  
}  
body : {  
    "status": "online",  
    "roles": ["admin"],  
    "canaux": [" "] // appel groupe propriétaire  
}  

* GET /seen/<pseudo> : dernière activité horodatée  
GET /seen/<pseudo> attente du groupe 2  

* GET /ison?users=roger,ginette : utilisateurs actuellement connectés  
GET /ison?users=nom1,nom2  
reponse body : {  
    nom1: true,  
    nom2: false  
}  

## Compléter : Gestion des profils
* PATCH /user/<pseudo>/password : changement de mot de passe (ancien + nouveau)  
header : {  
    Authorization: Bearer <le_token> // /!\ il faut renouveler le jwt  
}  
body : {  
    old-password: "" // mot de passe en clair ??  
    new-password: ""  
}  

* POST /user/status : changement de statut (away, idle, etc.)  
header : {  
    Authorization: Bearer <le_token>  
}  
body : {  
    new-statut: "idle"  
}  

* GET /user/avatar/<pseudo> : retourne l’URL (ou un avatar de test en base64)  
header : {  
    Authorization: Bearer <le_token>  
}  
body : {  
    url: ""   
}  

* DELETE /user/<pseudo> : suppression d’un compte  
header : {  
    Authorization: Bearer <le_token>  
}  

## Finaliser : Gestion des rôles
* GET /user/roles/<pseudo> : liste des rôles globaux (admin, user)  
body : {  
    roles: [role1, role2]  
}  

* POST /user/roles/<pseudo> : ajoute un rôle à un utilisateur (admin uniquement)  
header : {  
    Authorization: Bearer <le_token> // /!\ admin uniquement  
}  
body : {  
    role: "administrateur"  
}  

* Faire une fonction (ou une route particulière /make-admin/<pseudo> accessible uniquement aux admins via JWT)  
Route cachée !    
