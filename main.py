import discord
import sys
import os
       
intents = discord.Intents.default()  # 標準設定から
intents.typing = False  # typingは受け取らない
intents.message_content = True  # message_contentは受け取る
intents.members = True

guild = discord.Object(1082464517025431692)
 
client = discord.Client(intents=intents)
TOKEN = os.environ.get("DISCORD_TOKEN")
#"MTA4MjQ2MDkwNDA4NTUzMjcwMg.GGqNKd.ghXmAIzAuB4mp9PIycNzwmGG01FWAZUtW9IwA4"     
tree = discord.app_commands.CommandTree(client)

@tree.command(
    name="addroles",#コマンド名
    description="全員に特定のロールを付与します。",#コマンドの説明
    guild=guild)
async def addroles(ctx:discord.Interaction,roleschoice:discord.Role):
    if not ctx.user.guild_permissions.manage_roles:
        await ctx.response.send_message(f"実行する権限がありません",ephemeral = True)
        return
    await ctx.response.defer(ephemeral = True)
    for member in ctx.guild.members:
        if member.bot:
            continue
        await member.add_roles(roleschoice)
    await ctx.followup.send(f"メンバー全員に{roleschoice.name}を付与しました",ephemeral = True)
    
@tree.command(
    name="removeroles",#コマンド名
    description="全員から特定のロールを剥奪します。",#コマンドの説明
    guild=guild)
async def removeroles(ctx:discord.Interaction,roleschoice:discord.Role):
    if not ctx.user.guild_permissions.manage_roles:
        await ctx.response.send_message(f"実行する権限がありません",ephemeral = True)
        return
    await ctx.response.defer(ephemeral = True)
    for member in ctx.guild.members:
        if member.bot:
            continue
        await member.remove_roles(roleschoice)
    await ctx.followup.send(f"メンバー全員から{roleschoice.name}を剥奪しました",ephemeral = True)

@tree.command(
    name="addroles_to_roles",#コマンド名
    description="特定のロール所有者に特定のロールを付与します。",#コマンドの説明
    guild=guild)
async def addroles_to_roles(ctx:discord.Interaction,roleschoice:discord.Role):
    if not ctx.user.guild_permissions.manage_roles:
        await ctx.response.send_message(f"実行する権限がありません",ephemeral = True)
        return
    await ctx.response.defer(ephemeral = True)
    for member in ctx.guild.members:
        if member.bot:
            continue
        if not roleschoice in member.roles:
            continue
        await member.add_roles(roleschoice)
    await ctx.followup.send(f"指定のメンバーに{roleschoice.name}を付与しました",ephemeral = True)

@tree.command(
    name="removeroles_from_roles",#コマンド名
    description="特定のロール所有者から特定のロールを剥奪します。",#コマンドの説明
    guild=guild)
async def removeroles_from_roles(ctx:discord.Interaction,roleschoice:discord.Role):
    if not ctx.user.guild_permissions.manage_roles:
        await ctx.response.send_message(f"実行する権限がありません",ephemeral = True)
        return
    await ctx.response.defer(ephemeral = True)
    for member in ctx.guild.members:
        if member.bot:
            continue
        if not roleschoice in member.roles:
            continue
        await member.remove_roles(roleschoice)
    await ctx.followup.send(f"指定のメンバーから{roleschoice.name}を剥奪しました",ephemeral = True)

@tree.command(
    name="addroles_to_unroles",#コマンド名
    description="特定のロール非所有者に特定のロールを付与します。",#コマンドの説明
    guild=guild)
async def addroles_to_unroles(ctx:discord.Interaction,roleschoice:discord.Role):
    if not ctx.user.guild_permissions.manage_roles:
        await ctx.response.send_message(f"実行する権限がありません",ephemeral = True)
        return
    await ctx.response.defer(ephemeral = True)
    for member in ctx.guild.members:
        if member.bot:
            continue
        if roleschoice in member.roles:
            continue
        await member.add_roles(roleschoice)
    await ctx.followup.send(f"指定のメンバーに{roleschoice.name}を付与しました",ephemeral = True)

@tree.command(
    name="removeroles_from_unroles",#コマンド名
    description="特定のロール非所有者から特定のロールを剥奪します。",#コマンドの説明
    guild=guild)
async def removeroles_from_unroles(ctx:discord.Interaction,roleschoice:discord.Role):
    if not ctx.user.guild_permissions.manage_roles:
        await ctx.response.send_message(f"実行する権限がありません",ephemeral = True)
        return
    await ctx.response.defer(ephemeral = True)
    for member in ctx.guild.members:
        if member.bot:
            continue
        if roleschoice in member.roles:
            continue
        await member.remove_roles(roleschoice)
    await ctx.followup.send(f"指定のメンバーから{roleschoice.name}を剥奪しました",ephemeral = True)

@client.event
# clientの準備完了時に呼び出されるイベント
async def on_ready():
    sys.stdout.write("ready")
    await tree.sync(guild=guild)
    # await tree.sync()
    sys.stdout.write('ready')

client.run(TOKEN)
