import os,string

path = "C:\\Users\\dema1\\OneDrive\\Desktop\\PythLearn"
ld = os.listdir(path)

print(ld) #files + directories
print([x for x in ld if os.path.isfile(path+'\\'+x)]) # only files
print([x.name for x in os.scandir(path) if x.is_dir()]) # only directories

print(os.path.exists(path) and os.access(path,os.R_OK) and os.access(path,os.W_OK) and os.access(path,os.X_OK))
#check existance, readability,writability,executability

if(os.path.exists(path)): #relative path to the existing directory or file
    print(os.path.relpath(path))

with open("lab-6\sample.txt",'r') as file: #count lines in a file
    lines = file.readlines()
    print(len(lines))



with open("lab-6\\fill_sample.txt",'w') as file: #writing to a file
    for entry in list([1,2,3,4,5,6]):
        file.write(str(entry)+'\n')

for i in range(26): #creating 26 files in format (upper_alphabet_letter).txt
    alphabet = list(string.ascii_uppercase)
    file = open("lab-6\\text_files\\"+alphabet[i]+'.txt', 'w+')
    if i == 0: # some sample to be used in the next tasks
        file.write("Things to be copied")
    file.close()


with open("lab-6\\text_files\\A.txt", 'r') as file:
    text = file.read()
    with open("lab-6\\text_files\\B.txt", 'w') as file2: #copying stuff from A.txt to B.txt
        file2.write(text)
        file2.close()
    file.close()
    
open("lab-6\\text_files\\new_file_to_delete.txt", 'w+').close() #creating file in 1 line to delete via os.remove
path2 = "lab-6\\text_files\\new_file_to_delete.txt"
if os.path.exists(path2) and os.access(path2,os.W_OK) and os.access(path2,os.R_OK):
    os.remove(path2)