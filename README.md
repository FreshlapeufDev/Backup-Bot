━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
     DISCORD BACKUP BOT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔧 PRÉREQUIS :
- Avoir Python 3.8 ou plus installé
- Créer une application bot sur https://discord.com/developers/applications
- Copier votre token dans le script à la ligne :
    bot.run("VOTRE TOKEN ICI")

📦 INSTALLATION :
1. Ouvrez un terminal dans le dossier du bot
2. Tapez la commande suivante pour installer les modules :
    pip install discord.py aiohttp
3. Lancez le bot avec :
    python bot.py

🔐 PERMISSIONS :
- Le bot doit avoir les permissions ADMINISTRATEUR sur le serveur
- Seuls les administrateurs peuvent utiliser les commandes

🛠️ COMMANDES DISPONIBLES :

+backupall
→ Sauvegarde les rôles, salons et emojis du serveur
→ Sauvegarde créée dans le dossier /backups

+restore
→ Restaure les rôles, salons et emojis depuis /backups
→ ⚠️ Supprime tous les salons et rôles existants avant restauration

📁 FICHIERS GÉNÉRÉS DANS /backups :
- roles.json → Contient tous les rôles
- channels.json → Contient tous les salons
- emojis.json → Contient tous les emojis

📝 REMARQUES :
- Le bot NE sauvegarde PAS les messages
- Utilisez sur un serveur de test avant de l’utiliser sur un vrai serveur

Créé par Fresh la peuf❤

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
