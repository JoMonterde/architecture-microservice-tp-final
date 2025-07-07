---
titre: Architecture micro-service
sous-titre: TP FINAL - IRC
auteur: Romain COURBAIZE Jodie Monterde Alberto MOUNGONDO Morgane MICHEL
theme: Warsaw
lang: fr-FR
section-titles: false
fontsize: 10pt
couleur-type-1: true
rendu-type: papier
rendu-logo: 3il
---


# Premiers points : Gestion des comptes

— Implémenter la route POST /register : création de compte (pseudo, mot de passe hashé, email) : 

POST /register body : {
    peudo : "Morgane"
    email : "morgane@gmail.com"
    pwd : "H4iWy"
}
reponse : 201

— Implémenter la route POST /login : authentification et génération d’un JWT

POST /login body : {
    email : "morgane@gmail.com"
    pwd : "H4iWy"
}
reponse : 200
{
    jwt : " " 
}



# 
