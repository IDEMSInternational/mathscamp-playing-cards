import json

def get_translation_map(lang, name):
    if lang == "eng":
        return {}
    map = json.load(open(f"vmc-translation-pipeline/complete_carddeck/translations/{lang}/{name}.json"))
    return map

def translate(trmap, str):
    if not trmap:
        return str
    found = 0
    for k, v in trmap.items():
        if str.find(k) != -1:
            str = str.replace(k, v)
            found += 1
    if not found:
        print(f"No translation for '{str}' found.")
    return str