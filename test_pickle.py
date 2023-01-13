import pickle


class Bird(object):
    have_feather = True
    reproduction_method = 'egg'


summer = Bird()
pickle_string = pickle.dumps(summer)

with open('summer.pkl', 'wb') as f:
    f.write(pickle_string)

with open('summer.pkl', 'rb') as f:
    summer = pickle.load(f)

print(summer.have_feather)
print(summer.reproduction_method)

int2 = 5460
float2 = 3.1415926
bool2 = True
str2 = 'python'
list2 = [('zzr', 18), ('rzz', 19)]
tuple2 = (('zrz', 20))
set2 = {1, 2, 3}
dict2 = {'zzr': 18, 'rzz': 19, 'zrz': 20}
data = [int2, float2, bool2, str2, list2, tuple2, set2, dict2]
with open('sample_pickle.dat', 'wb') as f:
    try:
        pickle.dump(len(data), f)
        for item in data:
            pickle.dump(item, f)
    except:
        print("error")
