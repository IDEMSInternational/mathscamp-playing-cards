import csv
import json
import os
from shutil import copyfile, copytree
from translation_tools import get_translation_map, translate

LANG = 'fra'

def write_paragraph(title, content, out):
    insert_pos = content.find("<p>") + len("<p>")
    if insert_pos == -1:
        out.write("<b>" + title + ": </b> " + content + "\n\n")
    else:
        out.write(content[:insert_pos] + "<b>" + title + ": </b> " + content[insert_pos:] + "\n\n")

suits = {'H' : "hearts", "S" : "spades", "C" : "clubs", "D" : "diamonds"}

path = f"booklet/{LANG}/"
os.makedirs(path, exist_ok=True)
copytree("json/images", path+"images", dirs_exist_ok=True)
copyfile("booklet/booklet.css", path+"booklet.css")

out = open(path+"booklet.html", "w")
cardcsv = open('cards.csv')
reader = csv.reader(cardcsv)
for row in reader:
    out.write("""<link href="booklet.css" rel="stylesheet" type="text/css">\n\n""")
    card = row[0]
    filename = row[1].lower().replace(" ", "-")
    suit = suits[card[0]]
    rank = card[1:]
    trmap = get_translation_map(LANG, filename)

    with open("json/" + filename + ".json", "r") as read_file:
        print(filename)
        data = json.load(read_file)
        ctype = data["metadata"]["type"]
        if ctype == "counting":
            ctype = "puzzle"

        out.write("<h2> " + card + " - " + translate(trmap, data["title"]) + "</h2>\n\n")
        out.write(translate(trmap, data["main_version"]["statement"]) + "\n\n")
        if ctype == "puzzle" or ctype == "funfact":
            if "hint" in data["main_version"]:
                write_paragraph("Hint", translate(trmap, data["main_version"]["hint"]), out)
            write_paragraph("Explanation", translate(trmap, data["main_version"]["explanation"]), out)
        elif ctype == "game":
            write_paragraph("Further instructions", translate(trmap, data["main_version"]["further_instructions"]), out)
            write_paragraph("Strategy Tips", translate(trmap, data["main_version"]["strategy_tips"]), out)
        write_paragraph("About", translate(trmap, data["additional_information"]["about"]), out)
        out.write("<h3>Extension 1</h3>\n\n")
        out.write(translate(trmap, data["extension_1"]["statement"]) + "\n\n")
        if ctype == "puzzle" or ctype == "funfact":
            if "hint" in data["extension_1"]:
                write_paragraph("Hint", translate(trmap, data["extension_1"]["hint"]), out)
            if "explanation" in data["extension_1"]:
                write_paragraph("Explanation", translate(trmap, data["extension_1"]["explanation"]), out)
        if "extension_2" in data and "statement" in data["extension_2"]:
            out.write("<h3>Extension 2</h3>\n\n")
            out.write(translate(trmap, data["extension_2"]["statement"]) + "\n\n")
            if ctype == "puzzle" or ctype == "funfact":
                write_paragraph("Hint", translate(trmap, data["extension_1"]["hint"]), out)
                write_paragraph("Explanation", translate(trmap, data["extension_2"]["explanation"]), out)

cardcsv.close()
out.close()
