import json
import csv

finalFile = {}
with open('translation.csv', newline='') as f:
    reader = csv.reader(f)
    translationList = list(reader)

for index, item in enumerate(translationList):

    if item[2]:
        # finalFile = json.load(item)
        finalFile[item[0]] = item[2]
        finalFile['@' + item[0]] = {"description": item[2]}

        # print(mainData)
        # finalFile = json.dumps(mainData)

        # print (item, " at index ", index)
        # finalFile[item['key']] = item[3]
        # description = {}
        # description[item['description']] = item['Arabic']
        # finalFile['@'+item['key']] = description

print(finalFile)
