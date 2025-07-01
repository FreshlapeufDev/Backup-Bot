===============================
       DISCORD BACKUP BOT
===============================

DESCRIPTION  
Ce bot Discord permet de sauvegarder et restaurer la structure de votre serveur (rôles, salons, emojis) rapidement et facilement.  
Idéal pour les administrateurs qui veulent sécuriser leur serveur ou le réinitialiser rapidement.

FICHIERS INCLUS  
- bot.py          -> script principal du bot  
- start.bat       -> lance automatiquement le bot sous Windows  
- requirements.txt-> liste des dépendances Python  
- README.txt      -> ce fichier explicatif  

PRÉREQUIS  
- Python 3.x installé (https://www.python.org/downloads/)  
- Pip (gestionnaire de paquets Python) installé  
- Token du bot Discord (https://discord.com/developers/applications)  

INSTALLATION ET LANCEMENT  

1. Placez tous les fichiers dans un même dossier.

2. Installez les dépendances :  
   Ouvrez l’invite de commande (cmd) dans ce dossier et tapez :  
   pip install -r requirements.txt

3. Configurez le bot :  
   Ouvrez bot.py avec un éditeur de texte et remplacez la ligne :  
   bot.run("Votre token")  
   par :  
   bot.run("VOTRE_TOKEN_ICI")  
   en mettant le token de votre bot Discord à la place de VOTRE_TOKEN_ICI.

4. Lancez le bot :  
   Double-cliquez sur start.bat.  
   Une fenêtre console s’ouvrira, et vous verrez un message du type :  
   Connecté en tant que BotName

COMMANDES DISPONIBLES (ADMINISTRATEURS UNIQUEMENT)  

+backupall  
Sauvegarde la configuration complète du serveur :  
- Rôles (sauf @everyone)  
- Salons (textuels, vocaux, catégories)  
- Emojis personnalisés  
Les données sont enregistrées dans le dossier backups/ sous forme de fichiers JSON.

+restore  
Restaure le serveur à partir de la dernière sauvegarde :  
- Supprime les rôles et salons actuels (sauf @everyone)  
- Recrée les rôles, salons, catégories, emojis à partir des fichiers sauvegardés  
- Supprime ensuite le dossier backups/  

LIMITATIONS IMPORTANTES  
- Les permissions précises sur chaque salon ne sont pas sauvegardées ni restaurées.  
- Les messages dans les salons ne sont pas sauvegardés.  
- Les rôles et salons gérés par des bots externes ne sont pas pris en compte.  
- Certaines erreurs peuvent survenir si le bot n’a pas les permissions nécessaires.

ASTUCES  
- Toujours lancer +backupall avant de faire des modifications importantes sur le serveur.  
- Vérifiez que le bot ait bien les permissions administrateur pour éviter les erreurs.  
- Ne lancez +restore que si vous êtes sûr de vouloir recréer toute la structure du serveur.

DÉPENDANCES (requirements.txt)  
discord.py  
aiohttp

SUPPORT & DISTRIBUTION  
Ce bot est libre et gratuit. Vous pouvez le modifier et le redistribuer.

===============================
