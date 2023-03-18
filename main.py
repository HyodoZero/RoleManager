import discord
import sys
import os
       
intents = discord.Intents.default()  # 標準設定から
intents.typing = False  # typingは受け取らない
intents.message_content = True  # message_contentは受け取る
intents.members = True
 
client = discord.Client(intents=intents)
TOKEN = os.environ.get("DISCORD_TOKEN")
tree = discord.app_commands.CommandTree(client)

@tree.command(
    name="addroles",#コマンド名
    description="全員に特定のロールを付与します。",#コマンドの説明
    )
async def addroles(ctx:discord.Interaction,roleschoice:discord.Role):
    if not ctx.user.guild_permissions.manage_roles:
        await ctx.response.send_message(f"実行する権限がありません",ephemeral = True)
        return
    await ctx.response.defer(ephemeral = True)
    try:    
        for member in ctx.guild.members:
            if member.bot:
                continue
            await member.add_roles(roleschoice)
        embed = discord.Embed(color = 0x00ff00, title= "動作完了", description=f"以下のロールを全員に付与しました。\n**{roleschoice.name}**")
        await ctx.followup.send(embed=embed,ephemeral = True)
    except discord.errors.Forbidden as error:
        embed = discord.Embed(color = 0xff0000, title= "問題発生", description=f"以下の設定を確認してください。\n・「サーバー設定」→「ロール」を開く。\n・ロールの順序を入れ替え、「RoleManager」が操作したいロールよりも上にあるようにする。")
        await ctx.followup.send(embed=embed,ephemeral = True)
    
@tree.command(
    name="removeroles",#コマンド名
    description="全員から特定のロールを剥奪します。",#コマンドの説明
    )
async def removeroles(ctx:discord.Interaction,roleschoice:discord.Role):
    if not ctx.user.guild_permissions.manage_roles:
        await ctx.response.send_message(f"実行する権限がありません",ephemeral = True)
        return
    await ctx.response.defer(ephemeral = True)
    try:
        for member in ctx.guild.members:
            if member.bot:
                continue
            await member.remove_roles(roleschoice)
        embed = discord.Embed(color = 0x00ff00, title= "動作完了", description=f"以下のロールを全員から剥奪しました。\n**{roleschoice.name}**")
        await ctx.followup.send(embed=embed,ephemeral = True)
    except discord.errors.Forbidden as error:
        embed = discord.Embed(color = 0xff0000, title= "問題発生", description=f"以下の設定を確認してください。\n・「サーバー設定」→「ロール」を開く。\n・ロールの順序を入れ替え、「RoleManager」が操作したいロールよりも上にあるようにする。")
        await ctx.followup.send(embed=embed,ephemeral = True)
    

@tree.command(
    name="addroles_to_roles",#コマンド名
    description="特定のロール所有者に特定のロールを付与します。",#コマンドの説明
    )
async def addroles_to_roles(ctx:discord.Interaction,rolestarget:discord.Role,roleschoice:discord.Role):
    if not ctx.user.guild_permissions.manage_roles:
        await ctx.response.send_message(f"実行する権限がありません",ephemeral = True)
        return
    await ctx.response.defer(ephemeral = True)
    try:
        for member in ctx.guild.members:
            if member.bot:
                continue
            if not rolestarget in member.roles:
                continue
            await member.add_roles(roleschoice)
        embed = discord.Embed(color = 0x00ff00, title= "動作完了", description=f"以下のロールを指定のメンバーに付与しました。\n**{roleschoice.name}**")
        await ctx.followup.send(embed=embed,ephemeral = True)
    except discord.errors.Forbidden as error:
        embed = discord.Embed(color = 0xff0000, title= "問題発生", description=f"以下の設定を確認してください。\n・「サーバー設定」→「ロール」を開く。\n・ロールの順序を入れ替え、「RoleManager」が操作したいロールよりも上にあるようにする。")
        await ctx.followup.send(embed=embed,ephemeral = True)

@tree.command(
    name="removeroles_from_roles",#コマンド名
    description="特定のロール所有者から特定のロールを剥奪します。",#コマンドの説明
    )
async def removeroles_from_roles(ctx:discord.Interaction,rolestarget:discord.Role,roleschoice:discord.Role):
    if not ctx.user.guild_permissions.manage_roles:
        await ctx.response.send_message(f"実行する権限がありません",ephemeral = True)
        return
    await ctx.response.defer(ephemeral = True)
    try:
        for member in ctx.guild.members:
            if member.bot:
                continue
            if not rolestarget in member.roles:
                continue
            await member.remove_roles(roleschoice)
        embed = discord.Embed(color = 0x00ff00, title= "動作完了", description=f"以下のロールを指定のメンバーから剥奪しました。\n**{roleschoice.name}**")
        await ctx.followup.send(embed=embed,ephemeral = True)
    except discord.errors.Forbidden as error:
        embed = discord.Embed(color = 0xff0000, title= "問題発生", description=f"以下の設定を確認してください。\n・「サーバー設定」→「ロール」を開く。\n・ロールの順序を入れ替え、「RoleManager」が操作したいロールよりも上にあるようにする。")
        await ctx.followup.send(embed=embed,ephemeral = True)

@tree.command(
    name="addroles_to_missingroles",#コマンド名
    description="特定のロール非所有者に特定のロールを付与します。",#コマンドの説明
    )
async def addroles_to_missingroles(ctx:discord.Interaction,rolestarget:discord.Role,roleschoice:discord.Role):
    if not ctx.user.guild_permissions.manage_roles:
        await ctx.response.send_message(f"実行する権限がありません",ephemeral = True)
        return
    await ctx.response.defer(ephemeral = True)
    try:
        for member in ctx.guild.members:
            if member.bot:
                continue
            if rolestarget in member.roles:
                continue
            await member.add_roles(roleschoice)
        embed = discord.Embed(color = 0x00ff00, title= "動作完了", description=f"以下のロールを指定のメンバーに付与しました。\n**{roleschoice.name}**")
        await ctx.followup.send(embed=embed,ephemeral = True)
    except discord.errors.Forbidden as error:
        embed = discord.Embed(color = 0xff0000, title= "問題発生", description=f"以下の設定を確認してください。\n・「サーバー設定」→「ロール」を開く。\n・ロールの順序を入れ替え、「RoleManager」が操作したいロールよりも上にあるようにする。")
        await ctx.followup.send(embed=embed,ephemeral = True)

@tree.command(
    name="removeroles_from_missingroles",#コマンド名
    description="特定のロール非所有者から特定のロールを剥奪します。",#コマンドの説明
    )
async def removeroles_from_missingroles(ctx:discord.Interaction,rolestarget:discord.Role,roleschoice:discord.Role):
    if not ctx.user.guild_permissions.manage_roles:
        await ctx.response.send_message(f"実行する権限がありません",ephemeral = True)
        return
    await ctx.response.defer(ephemeral = True)
    try:
        for member in ctx.guild.members:
            if member.bot:
                continue
            if rolestarget in member.roles:
                continue
            await member.remove_roles(roleschoice)
        embed = discord.Embed(color = 0x00ff00, title= "動作完了", description=f"以下のロールを指定のメンバーから剥奪しました。\n**{roleschoice.name}**")
        await ctx.followup.send(embed=embed,ephemeral = True)
    except discord.errors.Forbidden as error:
        embed = discord.Embed(color = 0xff0000, title= "問題発生", description=f"ロール付与が正常に行われませんでした。\n以下の設定を確認してください。\n・「サーバー設定」→「ロール」を開く。\n・ロールの順序を入れ替え、「RoleManager」が操作したいロールよりも上にあるようにする。")
        await ctx.followup.send(embed=embed,ephemeral = True)

@tree.command(
    name="help",#コマンド名
    description="このbotの使い方です。",#コマンドの説明
    )
async def addroles_to_roles(ctx:discord.Interaction):
    if not ctx.user.guild_permissions.manage_roles:
        await ctx.response.send_message(f"実行する権限がありません",ephemeral = True)
        return
    embed = discord.Embed(color = 0x000000, title= "How to use", description=f"RoleManagerについて解説します。")
    embed.add_field(name="概要",value="このbotはサーバー内のメンバーへのロール付与を一括で行います。\nこのbotの機能は全て、\"/\"から始まるコマンドを入力することで実行されます。",inline=False)
    embed.add_field(name="使う前に",value="このbotを利用する前に、ロールの順位を設定する必要があります。\n・「サーバー設定」→「ロール」を開く。\n・ロールの順序を入れ替え、「RoleManager」が操作したいロールよりも上にあるようにする。",inline=False)
    embed.add_field(name="コマンド一覧",value="以下はこのbotで利用可能なコマンドです。",inline=False)
    embed.add_field(name="/addroles",value="このコマンドは、サーバー内の全員に特定のロールを付与します。",inline=False)
    embed.add_field(name="/removeroles",value="このコマンドは、サーバー内の全員から特定のロールを剥奪します。",inline=False)
    embed.add_field(name="/addroles_to_roles",value="このコマンドは、サーバー内の特定のロールを持っているメンバーに特定のロールを付与します。\n一つ目に入力したロールを持っているメンバーに、二つ目のロールを付与します。",inline=False)
    embed.add_field(name="/removeroles_from_roles",value="このコマンドは、サーバー内の特定のロールを持っているメンバーから特定のロールを剥奪します。\n一つ目に入力したロールを持っているメンバーから、二つ目のロールを剥奪します。",inline=False)
    embed.add_field(name="/addroles_to_missingroles",value="このコマンドは、サーバー内の特定のロールを持っていないメンバーに特定のロールを付与します。\n一つ目に入力したロールを持っていないメンバーに、二つ目のロールを付与します。",inline=False)
    embed.add_field(name="/addroles_from_missingroles",value="このコマンドは、サーバー内の特定のロールを持っていないメンバーから特定のロールを剥奪します。\n一つ目に入力したロールを持っていないメンバーから、二つ目のロールを剥奪します。",inline=False)
    await ctx.response.send_message(embed=embed,ephemeral = True)

@client.event
# clientの準備完了時に呼び出されるイベント
async def on_ready():
    sys.stdout.write("ready")
    await tree.sync()
    # await tree.sync()
    sys.stdout.write('ready')

client.run(TOKEN)
