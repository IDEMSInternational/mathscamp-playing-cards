import csv
import json
import os
import re
from shutil import copyfile, copytree

from translation_tools import get_translation_map, translate

LANG = 'eng'

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

suits = {'H' : "hearts", "S" : "spades", "C" : "clubs", "D" : "diamonds"}
path = f"cards/{LANG}/"
os.makedirs(path, exist_ok=True)
copytree("json/images", path+"images", dirs_exist_ok=True)
f = open("cards.csv", 'r')
reader = csv.reader(f)
for row in reader:
    card = row[0]
    if card[1:] == '1':
        card = card[0] + 'A'
    reverse_card = "{}{}".format(card[1:], card[0])
    filename = row[1].lower().replace(" ", "-")
    trmap = get_translation_map(LANG, filename)
    prefix = path + f"{card}_"
    copyfile(f"qrcodes/{LANG}/{reverse_card}.png", prefix+"qr_code.png")
    with open("json/" + filename + ".json", "r") as read_file:
        data = json.load(read_file)
        text = translate(trmap, data["main_version"]["statement"])
        # text = text.replace("src=\"images/", "src=\"")

        fhtml = open(prefix + 'content.html', 'w')
        fhtml.write(text)
        fhtml.close()

        # if text.find("<img") != -1:
        #     print(card + " has image.")

        ftxt = open(prefix + 'content.txt', 'w')
        ftxt.write(cleanhtml(text))
        ftxt.close()

        ftxt = open(prefix + 'chatbot_code.txt', 'w')
        ftxt.write("VMC_" + reverse_card)
        ftxt.close()
        # print("VMC_" + reverse_card)


f.close()