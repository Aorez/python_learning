import json

dic = {"b": 2, "a": 1, "c": 3}
jsonstr = json.dumps(dic)
print(jsonstr, type(jsonstr))
dic2 = json.loads(jsonstr)
print(dic2, type(dic2))
jsonstr = json.dumps(dic, sort_keys=True, indent=2)
print(jsonstr)

with open("test_beijing_aqi.json", mode='r', encoding='utf-8') as f:
    beijing_aqi = json.load(f)

sorted_key = 'aqi'
beijing_aqi_sorted = sorted(beijing_aqi, key=lambda x: x[sorted_key])

with open("test_beijing_aqi.csv", mode='w', encoding='utf-8') as f:
    f.write(','.join(list(beijing_aqi[0].keys())) + '\n')
    for i in beijing_aqi_sorted:
        f.write(','.join([str(j) for j in i.values()]) + '\n')
