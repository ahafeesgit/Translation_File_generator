import json
import csv

f = open('data.json')
data = json.load(f)
with open('to_translate.csv', mode='w') as toTranslateFile:
                writer = csv.writer(toTranslateFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                fieldnames = ['Content','key']
                writer = csv.DictWriter(toTranslateFile, fieldnames=fieldnames)
                writer.writeheader()
                for individual_data in data:

                    for key in individual_data.keys():
                    
                        if key.find('@') == -1:
                            print(individual_data[key])
                            writer.writerow({'Content':individual_data[key],'key':key})
