import json
import difflib

data = json.load(open("Data/data.json"))

def przeksztalcenie(slowo):
    slowo = slowo.lower()
    
    if slowo in data:
        return data[slowo]

    elif len(difflib.get_close_matches(slowo, data.keys(), n=5)) > 0:
        czyPoprawneSlowo = input("Did You mean \"%s\" ? If Yes type \"Y\" if No type \"N\".\n" % difflib.get_close_matches(slowo, data.keys())[0])

        if czyPoprawneSlowo == "Y":
            return przeksztalcenie(difflib.get_close_matches(slowo, data.keys())[0])

        elif czyPoprawneSlowo == "N":
            return "Your word is incorrect."

        else:
            return "Answer not correct."

    else:
        return "Your word is incorrect. Plese check it."

wejscie = input("Enter word: ")
wyjscie = przeksztalcenie(wejscie)
if type(wyjscie) == list:
    for item in wyjscie:
        print("%s \n" % item)
else:
    print(wyjscie)

