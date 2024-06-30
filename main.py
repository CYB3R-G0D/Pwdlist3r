from itertools import permutations

print("""
                   _ _ _     _   _____
 _ ____      ____| | (_)___| |_|___ / _ __
| '_ \ \ /\ / / _` | | / __| __| |_ \| '__|
| |_) \ V  V | (_| | | \__ | |_ ___) | |
| .__/ \_/\_/ \__,_|_|_|___/\__|____/|_|
|_|
# Generate user password wordlist for a brute-force attack
# Script by @cyb3r-g0d
# Thanks to Dhushyanth, Sam Godson
    """)

a = []

def get_input(prompt, min_length=1):
    value = input(prompt).strip().lower()
    while len(value) < min_length:
        print('\n[*] You must enter a valid input!')
        value = input(prompt).strip().lower()
    return value

def capitalize_variations(name):
    return [name, name.capitalize(), name.upper(), name[:3], name[:3].capitalize(), name[:3].upper()]

def date_variations(date):
    return [date, date[:2], date[2:4], date[4:6], date[6:], date[:4], date[-2:], date[-3:], date[-4:]]

first_name = get_input('First name: ')
second_name = input('Second name: ').strip().lower()
surname = input('Surname: ').strip().lower()
nickname = input('Nickname: ').strip().lower()
birthdate = input('Birthdate (DDMMYYYY): ').strip()

pfirst_name = input('Partner first name: ').strip().lower()
psecond_name = input('Partner second name: ').strip().lower()
psurname = input('Partner surname: ').strip().lower()
pnickname = input('Partner nickname: ').strip().lower()
pbirthdate = input('Partner birthdate (DDMMYYYY): ').strip()

cfirst_name = input('Child first name: ').strip().lower()
csecond_name = input('Child second name: ').strip().lower()
csurname = input('Child surname: ').strip().lower()
cnickname = input('Child nickname: ').strip().lower()
cbirthdate = input('Child birthdate (DDMMYYYY): ').strip()

petname = input('Pet name: ').strip().lower()

if input('Want to include special words? (y/n): ').strip().lower() == 'y':
    special_text = input('Enter special words separated by commas (e.g., professor,singer,flowers): ').replace(' ', '').lower()
    a.extend(special_text.split(','))

if input('Want to include special numbers? (y/n): ').strip().lower() == 'y':
    special_numbers = input('Enter special numbers separated by commas (e.g., 1,22,123): ').replace(' ', '').split(',')
    a.extend(special_numbers)

if input('Want to include special characters? (y/n): ').strip().lower() == 'y':
    special_characters = '!,@,#,$,%,^,&,*,(,),_,-,+'.split(',')
    a.extend(special_characters)

def permut():
    my_list = (
        capitalize_variations(first_name) +
        capitalize_variations(second_name) +
        capitalize_variations(surname) +
        capitalize_variations(nickname) +
        date_variations(birthdate) +
        capitalize_variations(pfirst_name) +
        capitalize_variations(psecond_name) +
        capitalize_variations(psurname) +
        capitalize_variations(pnickname) +
        date_variations(pbirthdate) +
        capitalize_variations(cfirst_name) +
        capitalize_variations(csecond_name) +
        capitalize_variations(csurname) +
        capitalize_variations(cnickname) +
        date_variations(cbirthdate) +
        capitalize_variations(petname)
    )
    my_list.extend(a)
    
    c = set()
    b = list(permutations(my_list, 2))
    
    for pair in b:
        if len(pair[0] + pair[1]) >= 6:
            c.add(pair[0] + pair[1])
    
    for k in my_list:
        for pair in b:
            if len(pair[0] + pair[1]) >= 6:
                c.add(pair[0] + k + pair[1])
                c.add(pair[0] + pair[1] + k)
                c.add(k + pair[0] + pair[1])
    
    return c

def save_to_file(filename, data):
    with open(filename, 'w') as file:
        file.write('\n'.join(data))

def remove_duplicates(filename):
    with open(filename, 'r') as file:
        lines = set(file.readlines())
    with open(filename, 'w') as file:
        file.writelines(lines)

filename = f'{first_name}.txt'
save_to_file(filename, permut())
remove_duplicates(filename)

print(f'Wordlist generated and saved to {filename}')
