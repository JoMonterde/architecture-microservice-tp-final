# Architecture micro-service - TP FINAL IRC - Groupe 1 : user-service 
- [x] POST /register Créer un compte utilisateur  
✅ Cas de réussite : Création d’un compte avec un pseudo, email et mot de passe valides  
Réponse : "status": "ok", "reponse": "Compte créé"  
❌ Cas d’erreur – Données manquantes : Email non renseigné / Pseudo non renseigné / Mot de passe non renseigné  
Réponse (400) :  
{  
  "status": "ko",  
  "reponse": "Erreur : pseudo et/ou email et/ou password manquant(s)"  
}  
❌ Cas d’erreur – Conflit (utilisateur déjà existant) : Pseudo ou email déjà utilisé  
Réponse (409) :  
{  
  "status": "ko",  
  "reponse": "Erreur : l'adresse e-mail {email} ou le pseudo {pseudo} est déjà utilisé."
}  

- [x] POST /login Authentifier et retourner un JWT  
✅ Cas de réussite : Authentification avec un pseudo et un mot de passe valides  
Réponse (200) :  
{  
  "status": "ok",  
  "reponse": {  
    "token": "eyJ0eXAiOiJKV1QiLCJhbGci..."  
  }  
}  
❌ Cas d’échec : Mot de passe valide mais pseudo incorrect  
Pseudo valide mais mot de passe incorrect  
Les deux incorrects  
Un seul champ renseigné (pseudo ou mot de passe)  
Mot de passe correct avec un pseudo qui n'est pas le sien  
Réponse (401) :  
{  
  "status": "ko",  
  "error": "Pseudo et/ou mot de passe invalide(s)"  
}  

- [ ] GET /whois/<pseudo> Infos publiques sur un utilisateur
✅ Cas de réussite : Récupération des informations : pseudo, rôle et channels associés  
Exemple de réponse (200) :  
{  
  "pseudo": "Morgane",  
  "role": "user",  
  "channels": ["canal1", "canal2"]  
}  
❌ Cas d’erreur – Utilisateur inexistant :  
Pseudo non trouvé dans la base  
Réponse :  
{  
  "status": "ko",  
  "error": "Pseudo non trouvé"  
}  
❌ Cas d’erreur – Champs manquants : L’un ou plusieurs des champs suivants ne sont pas renseignés (Email, Pseudo, Mot de passe)
Réponse attendue (400) :  
{  
  "status": "ko",  
  "reponse": "Erreur : pseudo et/ou email et/ou password manquant(s)"  
}  
❌ Cas d’erreur – Utilisateur déjà existant : Un pseudo déjà utilisé ou une adresse e-mail déjà utilisée  
Réponse attendue (409) :  
{  
  "status": "ko",  
  "reponse": "Erreur : l'adresse e-mail {email} ou le pseudo {pseudo} est déjà utilisé."  
}  
- [ ] GET /seen/<pseudo> Dernière activité horodatée
- [ ] GET /ison?users=roger,gineLtitsete des utilisateurs actuellement connectés
- [ ] PATCH /user/<pseudo>/passworCdhanger le mot de passe
- [ ] GET /user/avatar/<pseudo> Récupérer l’avatar
- [ ] DELETE/user/<pseudo> Supprimer un utilisateur
- [ ] GET /user/roles/<pseudo> Récupérer les rôles globaux
- [ ] POST /user/roles/<pseudo> Ajouter un rôle global (admin only)
- [ ] POST /make-admin/<pseudo> Donner le rôle admin (admin only,facultatif route)
