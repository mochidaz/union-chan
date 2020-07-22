from discord.ext import commands
from src.convertdata import sekantung_kata, kata, label, data, net
import random
import numpy
import tflearn
import sys

args = sys.argv[1]

model = tflearn.DNN(net)
model.load('./src/model/model.tfl')

client = commands.Bot(command_prefix='!union ')


class UnionChan:
    def __init__(self):
        self.is_on = False

    async def on_message_(self, msg):

        author = msg.author
        content = msg.content
        channel = msg.channel
        sender = channel
        debugchannel = client.get_channel("DEBUG CHANNEL ID")

        results = model.predict([sekantung_kata(content, kata)])
        results_index = numpy.argmax(results)
        tag = label[results_index]

        for tg in data["intents"]:
            if tg['tag'] == tag:
                responses = tg['responses']
        if self.is_on:
            if args == '--debug':
                if not author.bot and channel.id == debugchannel.id:
                    sender.send(random.choice(responses))

            elif args == '--start':
                if not author.bot:
                    sender.send(random.choice(responses))

    async def nyalakan_(self, ctx):
        self.is_on = True
        ctx.send('Menyalakan bot...')

    async def matikan_(self, ctx):
        self.is_on = False
        ctx.send('Mematikan bot...')


@client.event
async def on_message(msg):
    await UnionChan().on_message_(msg)

# Masih dalam pengembangan
@client.command()
async def nyalakan(ctx):
    await UnionChan().nyalakan_(ctx)

# Masih dalam pengembangan
@client.command()
async def matikan(ctx):
    await UnionChan().matikan_(ctx)


client.run('TOKEN')
