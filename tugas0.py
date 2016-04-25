from flask import Flask
import json
import os

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return json.dumps(sort)

filenya = os.listdir("../filenya/.")
listnya = filenya[((len(filenya)/2)-1):]

sentence = {}

for files in listnya:
    print files
    for line in open("../filenya/"+files).xreadlines():
        cek = line.split()
        cek = " ".join(cek[4:])

        if (cek in sentence):
            sentence[cek] += 1
        else:
            sentence[cek] = 0

sort = sorted(sentence.items(), key=lambda x:x[1], reverse=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0')