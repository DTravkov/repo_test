import psycopg2
from fill_data import *
first_name = ''
phone_number = ''
while True:
    print("\nEnter q to exit")
    first_name = str(input("---Enter first name of a person\n"))
    if first_name == 'q' or first_name == 'Q':
        break
    elif first_name == '' or first_name == None:
        print('\nIncorrect first name\n')
        continue

    else:
        phone_number = str(input(f"\n---Enter {first_name}'s phone number\n"))
        if phone_number == 'q' or phone_number == 'Q':
            break
        elif phone_number == '' or phone_number == None:
            print('\nIncorrect phone number\n')
            continue
    
    if first_name and phone_number:
        answer = input(f" {first_name}'s phone is {phone_number}.Is that right?\nEnter 'yes' or 'no' ")
        if answer == 'yes' or answer == 'Yes':
            insert_number(str(first_name),str(phone_number))
        else:
            continue