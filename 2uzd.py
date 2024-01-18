import csv

def lasit_otro_kolonnu(yo):
    with open(yo, 'r', newline='', encoding='utf-8') as f:
        ceesve = csv.reader(f)
        for rinda in ceesve:
            if len(rinda) > 1:
                print(rinda[1])


lasit_otro_kolonnu('yo.csv')