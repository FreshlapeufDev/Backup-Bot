import discord
from discord.ext import commands
import json
import os
import shutil
import aiohttp

intents = discord.Intents.default()
intents.members = True
intents.guilds = True
intents.message_content = True

bot = commands.Bot(command_prefix='+', intents=intents)

BACKUP_DIR = "backups"

def clear_backup_folder():
    if os.path.exists(BACKUP_DIR):
        shutil.rmtree(BACKUP_DIR)
    os.makedirs(BACKUP_DIR)

@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")
    if not hasattr(bot, 'session'):
        bot.session = aiohttp.ClientSession()

@bot.command()
@commands.has_permissions(administrator=True)
async def backupall(ctx):
    guild = ctx.guild
    clear_backup_folder()


    roles_data = []
    for role in guild.roles:
        if role.is_default():
            continue
        roles_data.append({
            "name": role.name,
            "color": role.color.value,
            "permissions": role.permissions.value,
            "hoist": role.hoist,
            "mentionable": role.mentionable,
            "position": role.position,
            "managed": role.managed
        })

    with open(f"{BACKUP_DIR}/roles.json", "w", encoding="utf-8") as f:
        json.dump(roles_data, f, indent=4)


    channels_data = []
    for channel in guild.channels:
        channels_data.append({
            "name": channel.name,
            "type": channel.type.value,  
            "category": channel.category.name if channel.category else None,
            "position": channel.position,
            "nsfw": getattr(channel, "nsfw", False),
            "bitrate": getattr(channel, "bitrate", None),
            "user_limit": getattr(channel, "user_limit", None),
            "topic": getattr(channel, "topic", None)
        })

    with open(f"{BACKUP_DIR}/channels.json", "w", encoding="utf-8") as f:
        json.dump(channels_data, f, indent=4)


    emojis_data = []
    for emoji in guild.emojis:
        emojis_data.append({
            "name": emoji.name,
            "animated": emoji.animated,
            "url": str(emoji.url)
        })

    with open(f"{BACKUP_DIR}/emojis.json", "w", encoding="utf-8") as f:
        json.dump(emojis_data, f, indent=4)

    await ctx.send("Backup complet enregistré dans le dossier `backups/`.")

@bot.command()
@commands.has_permissions(administrator=True)
async def restore(ctx):
    guild = ctx.guild
    backup_path = BACKUP_DIR


    roles_path = os.path.join(backup_path, "roles.json")
    channels_path = os.path.join(backup_path, "channels.json")
    emojis_path = os.path.join(backup_path, "emojis.json")

    if not (os.path.exists(roles_path) and os.path.exists(channels_path)):
        await ctx.send("Aucun backup trouvé pour ce serveur.")
        return


    with open(roles_path, "r", encoding="utf-8") as f:
        roles = json.load(f)
    with open(channels_path, "r", encoding="utf-8") as f:
        channels = json.load(f)
    emojis = []
    if os.path.exists(emojis_path):
        with open(emojis_path, "r", encoding="utf-8") as f:
            emojis = json.load(f)


    for role in guild.roles:
        if role.is_default() or role.managed:
            continue
        try:
            await role.delete()
        except Exception as e:
            print(f"Erreur suppression rôle {role.name} : {e}")


    for role_data in roles:
        try:
            perms = discord.Permissions(role_data["permissions"])
            await guild.create_role(
                name=role_data["name"],
                colour=discord.Colour(role_data["color"]),
                hoist=role_data["hoist"],
                permissions=perms,
                mentionable=role_data["mentionable"]
            )
        except Exception as e:
            print(f"Erreur création rôle {role_data['name']} : {e}")


    for channel in guild.channels:
        try:
            await channel.delete()
        except Exception as e:
            print(f"Erreur suppression salon {channel.name} : {e}")


    categories = {}
    for ch_data in channels:
        if ch_data["type"] == 4:  
            try:
                cat = await guild.create_category(ch_data["name"], position=ch_data["position"])
                categories[ch_data["name"]] = cat
            except Exception as e:
                print(f"Erreur création catégorie {ch_data['name']} : {e}")


    for ch_data in channels:
        if ch_data["type"] == 4:
            continue  

        category = categories.get(ch_data["category"])

        try:
            if ch_data["type"] == 0:  
                await guild.create_text_channel(
                    ch_data["name"],
                    topic=ch_data.get("topic"),
                    nsfw=ch_data.get("nsfw", False),
                    position=ch_data["position"],
                    category=category
                )
            elif ch_data["type"] == 2:  
                await guild.create_voice_channel(
                    ch_data["name"],
                    bitrate=ch_data.get("bitrate"),
                    user_limit=ch_data.get("user_limit"),
                    position=ch_data["position"],
                    category=category
                )
        except Exception as e:
            print(f"Erreur création salon {ch_data['name']} : {e}")


    for emoji_data in emojis:
        try:

            async with bot.session.get(emoji_data["url"]) as resp:
                if resp.status == 200:
                    img_bytes = await resp.read()
                    await guild.create_custom_emoji(name=emoji_data["name"], image=img_bytes)
        except Exception as e:
            print(f"Erreur création emoji {emoji_data['name']} : {e}")


    try:
        shutil.rmtree(BACKUP_DIR)
    except Exception as e:
        print(f"Erreur suppression dossier backups : {e}")

    await ctx.send(f"Restauration complète du serveur `{guild.name}` terminée et dossier `backups/` supprimé.")

@bot.event
async def on_close():
    if hasattr(bot, 'session'):
        await bot.session.close()

bot.run("Votre token")
