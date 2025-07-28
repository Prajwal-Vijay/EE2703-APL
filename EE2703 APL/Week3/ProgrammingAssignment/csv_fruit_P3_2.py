import io
import csv
def csv_countfruits(msg):
    sfp = io.StringIO(msg)
    reader = list(csv.reader(sfp))
    fruit_dict = {}
    for i in range(1, len(reader)):
        if reader[i][0] not in fruit_dict.keys():
            fruit_dict[reader[i][0]] = int(reader[i][1])
        else:
            fruit_dict[reader[i][0]] += int(reader[i][1])
            
    return fruit_dict
msg = """Fruit,Number
Apple,3
Orange,5
Banana,4
Apple,7
Apple,2
Banana,3
"""
X = csv_countfruits(msg)