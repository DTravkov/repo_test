import csv,re,os

with open("dataset.csv","r+") as file:
    reader = csv.reader(file)
    arr = []
    for i in reader:
        arr.append(i)
    print(arr[0])
    data = list(arr[1:])
    print("########################################")
    print(data[:5])
    print("########################################")
    unique_levels = set()
    for row in data:
        for entry in row:
            if re.match("^Level.*",entry):
                unique_levels.add(re.match("^Level.*",entry).group())
    print(unique_levels,len(unique_levels))
    print("########################################")
    unique_industries = set()
    for row in data:
        unique_industries.add(row[3])
    print(unique_industries,len(unique_industries))
    print("########################################")
    unique_years = set()
    for row in data:
        unique_years.add(row[0])
    for i in unique_years:
        with open(f"{i}.csv","w+",newline = '') as yearfile:
            writer = csv.writer(yearfile)
            for row in data:
                if i == row[0]:
                    writer.writerow(row)
print("########################################")
list_of_files = [file for file in os.listdir("./") if file.endswith(".csv")]
print(list_of_files)
    