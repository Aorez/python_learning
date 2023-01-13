import csv
import json

with open('Dylan_van_Baarle.txt', 'r') as f:
    data = f.read()
    start = data.find('"evt"')
    end = data.find('}]},"swimLengthList":null}};')
    data = data[start:end]
    data = data.split('},{')

with open('train_DvB.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['ms', 'speed', 'elevation', 'temperature', 'cadence', 'power', 'distance', 'positional'])

    for i in data:
        data_dict = json.loads('{' + i + '}')
        writer.writerow([data_dict['ms'], data_dict['values'][1], data_dict['values'][2], data_dict['values'][3], data_dict['values'][4], data_dict['values'][5], data_dict['values'][6], data_dict['values'][7]])
