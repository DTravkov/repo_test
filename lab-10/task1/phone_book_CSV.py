import csv
from fill_data import *
path = input("\nEnter the name of the csv file you'd like to import\nMake sure the csv file is in the folder with this script\n")

pairs = []
with open(path,'r') as file:
    reader = csv.reader(file)
    fields = next(file)
    for i in reader:
        pairs.append(i)
    file.close()
print("Below are all the pairs in csv file\n")
for pair in pairs:
    print(pair[0],pair[1])
print('\n')


while True:
    answer = input("Do you want to insert all the data into PhoneBook?\nEnter 'yes' or 'no' ")
    if answer == 'yes' or answer == 'Yes':
        for pair in pairs:
            insert_number(pair[0],pair[1])
        break
    elif answer == 'no' or answer == 'No':
        break
    else:
        continue

    




