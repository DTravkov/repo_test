import json



jsonpath = r"C:\Users\dema1\OneDrive\Desktop\repo_test\lab-4\JSON\sample-data.json" # Copied JSON path as is

with open(jsonpath, "r") as file: 
    data = json.load(file)


datatf = [] # This guy will store lists of parsed data (only those values we need)


for i in data['imdata']: # Collecting data primitively
    object = i['l1PhysIf']['attributes']
    new_list = [] # Grouping up the data
    new_list.append(object['dn'])
    new_list.append(object['descr'])
    new_list.append(object['speed'])
    new_list.append(object['mtu'])
    datatf.append(new_list)


print("Interface Status")
print('=' * 100)
print(f"{'DN':<50} {'Description':<20} {'Speed':<10} {'MTU':<10}")
print(f"{'-' * 43} {'-' * 24} {'-' * 12} {'-' * 6} {'-' * 11}")
for i in datatf:
    print(f'{i[0]:<50} {i[1]:<20} {i[2]:<10} {i[3]:<10}')

