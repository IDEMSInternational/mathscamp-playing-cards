import json

def get_translation_map(lang, name):
    if lang in "eng":
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

all_fields = [
    ["title"],
    ["metadata", "type"],
    ["main_version", "statement"],
    ["main_version", "correct_answer"],
    ["main_version", "hint"],
    ["main_version", "explanation"],
    ["main_version", "further_instructions"],
    ["main_version", "strategy_tips"],
    ["extension_1", "statement"],
    ["extension_1", "hint"],
    ["extension_1", "correct_answer"],
    ["extension_1", "explanation"],
    ["extension_2", "statement"],
    ["extension_2", "hint"],
    ["extension_2", "correct_answer"],
    ["extension_2", "explanation"],
    ["additional_information", "about"],
    ["additional_information", "references"],
]

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
    ["extension_2", "hint"],
    ["extension_2", "explanation"],
]
