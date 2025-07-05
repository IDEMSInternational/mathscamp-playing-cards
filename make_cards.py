import csv
import json
import os
import re
from shutil import copyfile, copytree

from translation_tools import fields_to_translate, all_fields, get_translation_map, translate

LANGUAGES = [
    ['fr', 'fra'],
    ['en', 'eng'],
]

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

def make_cards(LANG, LANG3):
    suits = {'H' : "heart", "S" : "spade", "C" : "club", "D" : "diamond"}
    path = f"cards/{LANG}/"
    path_web = f"website/assets/"
    path_web_content = f"website/assets/card-content/{LANG}/"
    os.makedirs(path, exist_ok=True)
    os.makedirs(path_web_content + "cards", exist_ok=True)
    copytree("json/images", path+"images", dirs_exist_ok=True)
    copytree("json/images", path_web+"images", dirs_exist_ok=True)
    metadata = []
    f = open("cards.csv", 'r')
    reader = csv.reader(f)
    for row in reader:
        card = row[0]
        if card[1:] == '1':
            card = card[0] + 'A'
        reverse_card = "{}{}".format(card[1:], card[0])

        print(f"{reverse_card} -- {LANG3}")

        filename = row[1].lower().replace(" ", "-")
        trmap = get_translation_map(LANG3, filename)
        prefix = path + f"{card}_"
        copyfile(f"qrcodes/{LANG3}/{reverse_card}.png", prefix+"qr_code.png")
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

            # Web version files
            metadata.append(
                {
                    "title": translate(trmap, data["title"]),
                    "type": data["metadata"]["type"],
                    "slug": reverse_card,
                    "card_value": card[1:],
                    "card_suit": suits[card[0]],
                }
            )

            translated = {}
            for fields in all_fields:
                entry = data
                entry_t = translated
                last_field = None
                for i, field in enumerate(fields):
                    entry = entry.get(field, {})
                    if not entry:
                        continue
                    if field not in entry_t:
                        entry_t[field] = {}
                    if i < len(fields)-1:
                        entry_t = entry_t[field]
                    last_field = field
                if entry:
                    if fields in fields_to_translate:
                        entry_t[last_field] = translate(trmap, entry).replace("src=\"images/", "src=\"assets/images/")
                    elif fields == ["additional_information", "references"]:
                        entry_t[last_field] = [
                            re.sub(r"<p>(.+?)</p>", r'<p><a href="\1" target="_blank">\1</a></p>', line)
                            for line in entry
                        ]
                    else:
                        entry_t[last_field] = entry
            with open(path_web_content + f"cards/{reverse_card}.json", 'w') as web_card:
                json.dump(translated, web_card, indent=2)

    f.close()
    with open(path_web_content + "metadata.json", 'w') as web_meta:
        json.dump(metadata, web_meta, indent=2)

for lang, lang3 in LANGUAGES:
    make_cards(lang, lang3)