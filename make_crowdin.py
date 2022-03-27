import csv
import json
import re
from bs4 import BeautifulSoup, NavigableString
import os

def process_entry(content, out):
    soup = BeautifulSoup(content, features="html.parser")
    paragraphs = soup.find_all('p')
    for c in soup.contents:
        if type(c) == NavigableString:
            string = str(c)
        else:
            assert c.name == 'p'
            string = ''.join(str(t) for t in c.contents if t.name != 'img')
        string = string.strip()
        if string:
            out[string] = string

fields_to_translate = [
    ["title"],
    ["main_version", "statement"],
    ["main_version", "hint"],
    ["main_version", "explanation"],
    ["main_version", "further_instructions"],
    ["main_version", "strategy_tips"],
    ["additional_information", "about"],
    ["extension_1", "statement"],
    ["extension_1", "hint"],
    ["extension_1", "explanation"],
    ["extension_2", "statement"],
    ["extension_1", "hint"],
    ["extension_2", "explanation"],
]

os.makedirs('crowdin/cards/en-GB', exist_ok=True)
cardcsv = open('cards.csv')
reader = csv.reader(cardcsv)
for row in reader:
    filename = row[1].lower().replace(" ", "-")

    out = {}
    with open("json/" + filename + ".json", "r") as read_file:
        data = json.load(read_file)
        for fields in fields_to_translate:
            entry = data
            for field in fields:
                entry = entry.get(field, {})
            if entry:
                process_entry(entry, out)
    json.dump(out, open("crowdin/cards/en-GB/" + filename + ".json", "w"), indent=2)
