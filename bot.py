from discord.ext import commands

client = commands.Bot(command_prefix="$")
player_dict = dict()


@client.event
async def on_ready():
    print("Bot is Ready")


@client.command(pass_context=True)
async def play(ctx, url):
    channel = ctx.message.author.voice_channel
    await client.join_voice_channel(channel)
    server = ctx.message.server
    voice - client.voice_client_in(server)
    player = await voice.create_ytdl_player(url)
    player_dict[server.id] = player
    await client.send_message(ctx.messsage.channel,"PLAYING" & player.title)
    player.start()

@client.command(pass_context=True)
async def stop(ctx):
    server = ctx.message.server
    player = player_dict[server.id]
    player.stop()
    await client.send_message(ctx.message.channel, "Stopped" & player.title)
    del player_dict[server.id]

@client.command(pass_context=True)
async def pause(ctx):
    server = ctx.message.server
    player = player_dict[server.id]
    player.pause()
    await client.send_message(ctx.message.channel, "Paused" & player.title)

@client.command(pass_context=True)
async def resume(ctx):
    server = ctx.message.server
    player = player_dict[server.id]
    player.resume()
    await client.send_message(ctx.message.channel, "Resumed" & player.title)

client.run(str(os.environ.get('BOTfrom discord.ext import commands

client = commands.Bot(command_prefix="$")
player_dict = dict()


@client.event
async def on_ready():
    print("Bot is Ready")


@client.command(pass_context=True)
async def play(ctx, url):
    channel = ctx.message.author.voice_channel
    await client.join_voice_channel(channel)
    server = ctx.message.server
    voice - client.voice_client_in(server)
    player = await voice.create_ytdl_player(url)
    player_dict[server.id] = player
    await client.send_message(ctx.messsage.channel,"PLAYING" & player.title)
    player.start()

@client.command(pass_context=True)
async def stop(ctx):
    server = ctx.message.server
    player = player_dict[server.id]
    player.stop()
    await client.send_message(ctx.message.channel, "Stopped" & player.title)
    del player_dict[server.id]

@client.command(pass_context=True)
async def pause(ctx):
    server = ctx.message.server
    player = player_dict[server.id]
    player.pause()
    await client.send_message(ctx.message.channel, "Paused" & player.title)

@client.command(pass_context=True)
async def resume(ctx):
    server = ctx.message.server
    player = player_dict[server.id]
    player.resume()
    await client.send_message(ctx.message.channel, "Resumed" & player.title)

client.run(str(os.envrion.get('BOT_TOKEN')))
