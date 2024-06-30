from itertools import permutations

# Input data
first_name = 'emmitt'
second_name = 'romano'
surname = 'howard'
birthdate = '15081947'

pfirst_name = 'melissa'
psecond_name = 'hoggan'
pnickname = 'davis'
pbirthdate = '01051959'

petname = 'baibre'

special_text = 'flowers,fish,goat'
special_num = '1,22,123'

# Functions to generate variations
def capitalize_variations(name):
    return [name, name.capitalize(), name[:3], name[:3].capitalize()]

def date_variations(date):
    return [
        date, date[:2], date[2:4], date[4:6], date[6:], date[:4], date[-2:], date[-3:], date[-4:]
    ]

# Generate permutations
def permut():
    a = (
        capitalize_variations(first_name) +
        capitalize_variations(second_name) +
        capitalize_variations(surname) +
        date_variations(birthdate) +
        capitalize_variations(pfirst_name) +
        capitalize_variations(psecond_name) +
        capitalize_variations(pnickname) +
        date_variations(pbirthdate) +
        [petname, petname.capitalize(), petname[:3], petname[:3].capitalize()]
    )

    special_word = special_text.split(',')
    special_numbers = special_num.split(',')
    
    a.extend(special_word)
    a.extend(special_numbers)
    
    c = []
    b = list(permutations(a, 2))
    
    for pair in b:
        if len(pair[0] + pair[1]) >= 6:
            c.append(pair[0] + pair[1])
    
    return c

# Save permutations to file and remove duplicates
def save_to_file(filename, data):
    with open(filename, 'w') as file:
        for item in data:
            file.write(f"{item}\n")

def remove_duplicates(filename):
    with open(filename, 'r') as file:
        lines = set(file.readlines())
    with open(filename, 'w') as file:
        file.writelines(lines)

# File operations
filename = f'{first_name}.txt'
wordlist = permut()
save_to_file(filename, wordlist)
remove_duplicates(filename)

print(f'Wordlist generated and saved to {filename}')
