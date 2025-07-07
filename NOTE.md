titre: Architecture micro-service
sous-titre: TP FINAL - IRC
auteur: Romain COURBAIZE Jodie Monterde Alberto MOUNGONDO Morgane MICHEL


# Premiers points : Gestion des comptes

## Implémenter la route POST /register : création de compte (pseudo, mot de passe hashé, email) : 
POST /register body {
    "pseudo": "Morgane",
    "email": "morgane@gmail.com",
    "pwd": "H4iWy"
}
reponse : 201 Created : Le compte a été créé avec succès

## Implémenter la route POST /login : authentification et génération d’un JWT : 

POST /login body {
    "email": "morgane@gmail.com",
    "pwd": "H4iWy"
}
reponse : 200 OK
{
    "jwt" : "Authorization: Bearer <le_token>" 
}

## Utiliser un secret JWT dans les variables d’environnement
## Durée d’expiration du token configurable : 
Choix de 2 heures 

# Un peu plus en détail : Informations sur les utilisateurs

## GET /whois/<pseudo> : informations publiques (status, canaux, rôles)

GET /whois/<pseudo> 
header : {

}
reponse : 200 OK 
body : {
    "status": "online"
    "roles": ["admin"]
    "canaux": [" "] // 
}
## GET /seen/<pseudo> : dernière activité horodatée

GET /seen/<pseudo> att

## GET /ison?users=roger,ginette : utilisateurs actuellement connectés

GET /ison?users=nom1,nom2
reponse body : {
    "nom1": true
    "nom2": false 
}
