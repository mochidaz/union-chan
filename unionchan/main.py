from discord.ext import commands
from utils.utils import sekantung_kata, kata, label, data, net
import random
import numpy
import tflearn
import sys

args = sys.argv[1]

model = tflearn.DNN(net)
model.load('model/model.tfl')

client = commands.Bot(command_prefix='!union ')

global is_on
is_on = False

@client.event
async def on_message(msg):
    author = msg.author
    content = msg.content
    channel = msg.channel
    sender = channel
    debugchannel = client.get_channel("debug channel id")

    results = model.predict([sekantung_kata(content, kata)])
    results_index = numpy.argmax(results)
    tag = label[results_index]

    for tg in data["intents"]:
        if tg['tag'] == tag:
            responses = tg['responses']

    if "!union" in content:
        await client.process_commands(msg)

    else:
        if is_on:
            if args == '--debug':
                if not author.bot and channel.id == debugchannel.id:
                    await sender.send(random.choice(responses))

            elif args == '--start':
                if not author.bot:
                    await sender.send(random.choice(responses))
        else:
            pass


@client.command()
async def nyalakan(ctx):
    global is_on
    is_on = True
    await ctx.send("Menyalakan bot...")

@client.command()
async def matikan(ctx):
    global is_on
    is_on = False
    await ctx.send("Mematikan bot...")


client.run('TOKEN')
