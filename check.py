import json
with open("intents.json",r)as f:
    jsonDict = json.load(f)
test = jsonDict["intents"]
tagName = []
for tag in test:
    tagName.append(tag["responses"])
print(tagName)
print(len(tagName))
