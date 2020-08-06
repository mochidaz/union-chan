import numpy
import tflearn
import tensorflow
import json
import random
import datetime
from utils.utils import net, label, kata, data, sekantung_kata

model = tflearn.DNN(net)
model.load("model/model.tfl")


def chat():
    while True:
        content = str(input("Pengguna: "))
        if content == "dadah":
            exit()
        results = model.predict([sekantung_kata(content, kata)])
        results_index = numpy.argmax(results)
        tag = label[results_index]
        print(tag)

        if tag == 'datainteraksi-waktu':
            print("Union-chan: ", datetime.datetime.now())

        else:
            for tg in data["intents"]:
                if tg['tag'] == tag:
                    responses = tg['responses']

            print("Union-chan: ",random.choice(responses))

if __name__ == '__main__':
    chat()
