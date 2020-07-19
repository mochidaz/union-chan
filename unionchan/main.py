from discord.ext import commands
from unionchan.utils.utils import toString
from unionchan.src.convertdata import sekantung_kata, kata, label, data, net
import random
import numpy
import tflearn

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

        if not author.bot:
            results = model.predict([sekantung_kata(content, kata)])
            results_index = numpy.argmax(results)
            tag = label[results_index]

            for tg in data["intents"]:
                if tg['tag'] == tag:
                    responses = tg['responses']

            await sender.send(random.choice(responses))

    async def nyalakan_(self, ctx):
        self.is_on = True
        await ctx.send('Menyalakan bot...')

    async def matikan_(self, ctx):
        self.is_on = False
        await ctx.send('Mematikan bot...')


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
