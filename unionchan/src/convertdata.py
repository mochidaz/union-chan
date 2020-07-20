import nltk
from nltk.stem.lancaster import LancasterStemmer
import numpy
import tflearn
import tensorflow
import json
import sys

stemmer = LancasterStemmer()

nltk.download('punkt')

try:
    with open("data/conversation.json") as file:
        data = json.load(file)
except FileNotFoundError: # Untuk debugging dan training, karena bila file ini dirun, bukan dari main.py, maka python akan mendeteksi 'data/conversation.json'
    with open("src/data/conversation.json") as file:
        data = json.load(file)

kata = []
label = []
docs_x = []
docs_y = []

for inten in data["intents"]:
    for pola in inten["patterns"]:
        kata_ = nltk.word_tokenize(pola)
        kata.extend(kata_)
        docs_x.append(kata_)
        docs_y.append(inten["tag"])

    if inten["tag"] not in label:
        label.append(inten["tag"])

kata = [stemmer.stem(k.lower()) for k in kata if k != "?"]
kata = sorted(list(set(kata)))

label = sorted(label)

training = []
output = []

out_empty = [0 for _ in range(len(label))]

for x, doc in enumerate(docs_x):
    kantung = []

    kata_ = [stemmer.stem(w.lower()) for w in doc]

    for w in kata:
        if w in kata_:
            kantung.append(1)
        else:
            kantung.append(0)

    output_row = out_empty[:]
    output_row[label.index(docs_y[x])] = 1

    training.append(kantung)
    output.append(output_row)

training = numpy.array(training)
output = numpy.array(output)

tensorflow.reset_default_graph()

net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

def Model():
    model = tflearn.DNN(net)

    model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
    try:
        model.save("src/model/model.tfl")
    except ValueError:
        model.save("model/model.tfl")


def sekantung_kata(s, kata):
    kantung = [0 for i in range(len(kata))]

    s_kata = nltk.word_tokenize(s)
    s_kata = [stemmer.stem(kata.lower()) for kata in s_kata]

    for se in s_kata:
        for j, k in enumerate(kata):
            if k == se:
                kantung[j] = 1

    return numpy.array(kantung)

# Untuk generate model baru bila data sudah diupdate
if __name__ == '__main__':
    Model()
