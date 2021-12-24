
from itertools import permutations

print("""
                  _ _ _     _   _____
 _ ____      ____| | (_)___| |_|___ / _ __
| '_ \ \ /\ / / _` | | / __| __| |_ \| '__|
| |_) \ V  V | (_| | | \__ | |_ ___) | |
| .__/ \_/\_/ \__,_|_|_|___/\__|____/|_|
|_|
# generate user password wordlist for a brute-force attack
# script by @cyb3r-g0d
# thanks to Dhushyanth, Sam Godson
    """)

a = []

first_name = input('First name: ').lower()
while len(first_name) == 0 or first_name == ' ' or first_name == '  ' or first_name == '   ' or first_name == '    ' or first_name == '     ':
    print('\n''[*]You must enter a name at least!')
    first_name = input('First name: ').lower()
first_name_c = first_name.capitalize()
first_name_u = first_name.upper()
first_name_3 = first_name[:3]
first_name_3_c = first_name_3 .capitalize()
first_name_3_u = first_name_3 .upper()


second_name = input('Second name: ').lower()
second_name_3 = second_name[:3]
second_name_c = second_name.capitalize()
second_name_u = second_name.upper()
second_name_3_c = second_name_3.capitalize()
second_name_3_u = second_name_3.upper()

surname = input('Surname: ').lower()
surname_3 = surname[:3]
surname_c = surname.capitalize()
surname_u = surname.upper()
surname_3_c = surname_3.capitalize()
surname_3_u = surname_3.upper()

nickname = input('Nickname: ').lower()
nickname_3 = nickname[:3]
nickname_c = nickname.capitalize()
nickname_u = nickname.upper()
nickname_3_c = nickname_3.capitalize()
nickname_3_u = nickname_3.upper()

birthdate = input('birthdate (DDMMYYYY): ')
while len(birthdate) != 0 and len(birthdate) != 8:
    print('\n''[*]You must enter 8 digit for birthday!')
    birthdate = input("Birthdate (DDMMYYYY): ")
birthdate_d = birthdate[:1]
birthdate_dd = birthdate[:2]
birthdate_m = birthdate[3:4]
birthdate_mm = birthdate[2:4]
birthdate_y = birthdate[4:6]
birthdate_yy = birthdate[-2:]
birthdate_yyy = birthdate[-3:]
birthdate_yyyy = birthdate[-4:]

print('\n')

pfirst_name = input('Partner first name: ').lower()
pfirst_name_3 = pfirst_name[:3]
pfirst_name_c = pfirst_name.capitalize()
pfirst_name_3_c = pfirst_name_3.capitalize()
pfirst_name_u = pfirst_name.upper()
pfirst_name_3_u = pfirst_name_3.upper()

psecond_name = input('Partner second name: ').lower()
psecond_name_3 = psecond_name[:3]
psecond_name_c = psecond_name.capitalize()
psecond_name_3_c = psecond_name_3.capitalize()
psecond_name_u = psecond_name.upper()
psecond_name_3_u = psecond_name_3.upper()

psurname = input('Partner surname: ').lower()
psurname_3 = psurname[:3]
psurname_c = psurname.capitalize()
psurname_3_c = psurname_3.capitalize()
psurname_u = psurname.upper()
psurname_3_u = psurname_3.upper()

pnickname = input('Partner nickname: ').lower()
pnickname_3 = pnickname[:3]
pnickname_c = pnickname.capitalize()
pnickname_3_c = pnickname_3.capitalize()
pnickname_u = pnickname.upper()
pnickname_3_u = pnickname_3.upper()

pbirthdate = input('Partner birthdate (DDMMYYYY): ')
pbirthdate_d = pbirthdate[:1]
pbirthdate_dd = pbirthdate[:2]
pbirthdate_m = pbirthdate[3:4]
pbirthdate_mm = pbirthdate[2:4]
pbirthdate_y = pbirthdate[4:6]
pbirthdate_yy = pbirthdate[-2:]
pbirthdate_yyy = pbirthdate[-3:]
pbirthdate_yyyy = pbirthdate[-4:]

print('\n')

cfirst_name = input('Child first name: ').lower()
cfirst_name_3 = cfirst_name[:3]
cfirst_name_c = cfirst_name.capitalize()
cfirst_name_3_c = cfirst_name_3.capitalize()
cfirst_name_u = cfirst_name.upper()
cfirst_name_3_u = cfirst_name_3.upper()

csecond_name = input('Child second name: ').lower()
csecond_name_3 = csecond_name[:3]
csecond_name_c = csecond_name.capitalize()
csecond_name_3_c = csecond_name_3.capitalize()
csecond_name_u = csecond_name.upper()
csecond_name_3_u = csecond_name_3.upper()

csurname = input('Child surname: ').lower()
csurname_3 = csurname[:3]
csurname_c = csurname.capitalize()
csurname_3_c = csurname_3.capitalize()
csurname_u = csurname.upper()
csurname_3_u = csurname_3.upper()

cnickname = input('Child nickname: ').lower()
cnickname_3 = cnickname[:3]
cnickname_c = cnickname.capitalize()
cnickname_3_c = cnickname_3.capitalize()
cnickname_u = cnickname.upper()
cnickname_3_u = cnickname_3.upper()

cbirthdate = input('Child birthdate (DDMMYYYY): ')
cbirthdate_d = cbirthdate[:1]
cbirthdate_dd = cbirthdate[:2]
cbirthdate_m = cbirthdate[3:4]
cbirthdate_mm = cbirthdate[2:4]
cbirthdate_y = cbirthdate[4:6]
cbirthdate_yy = cbirthdate[-2:]
cbirthdate_yyy = cbirthdate[-3:]
cbirthdate_yyyy = cbirthdate[-4:]

print('\n')

petname = input('Pet name: ').lower()
petname_3 = petname[:3]
petname_c = petname.capitalize()
petname_3_c = petname_3.capitalize()
petname_u = petname.upper()
petname_3_u = petname_3.upper()

print('\n')

stext = input('want to include special words? (y/n): ')
if stext == 'y':
    special_text = input(
        'Please enter the some special words, separated by comma. [i.e. professor,singer,flowers], spaces will be removed: ').lower()
    special_word = special_text.split(',')
    for i in special_word:
        a.append(i)
else:
    pass

print('\n')

snum = input('want to include special numbers? (y/n): ')
if snum == 'y':
    special_num = input(
        'Please enter some special numbers, separated by comma. [i.e. 1,22,123], spaces will be removed: ').split(',')
    for x in special_num:
        a.append(x)
else:
    pass

print('\n')

schar = input('want to include special character? (y/n): ')
if schar == 'y':
    special_char = '!,@,#,$,%,^,&,*,(,),_,-,+'.split(',')
    if len(special_char) == 0:
        pass
    else:
        p = 1
    for x in special_char:
        a.append(x)
else:
    pass


def permut():
    my_list = [first_name, first_name_c, first_name_u, first_name_3, first_name_3_c, first_name_3_u,
        second_name, second_name_3, second_name_c, second_name_u, second_name_3_c, second_name_3_u,
        surname, surname_3, surname_c, surname_3_c, surname_u, surname_3_u,
        birthdate, birthdate_d, birthdate_dd, birthdate_m, birthdate_mm, birthdate_y, birthdate_yy, birthdate_yyy, birthdate_yyyy,
        pfirst_name, pfirst_name_c, pfirst_name_u, pfirst_name_3, pfirst_name_3_c, pfirst_name_3_u,
        psecond_name, psecond_name_3, psecond_name_c, psecond_name_3_c, psecond_name_u, psecond_name_3_u,
        psurname, psurname_3, psurname_c, psurname_3_c, psurname_u, psurname_3_u,
        pbirthdate, pbirthdate_d, pbirthdate_dd, pbirthdate_m, pbirthdate_mm, pbirthdate_y, pbirthdate_yy, pbirthdate_yyy, pbirthdate_yyyy,
        petname, petname_3, petname_c, petname_3_c, petname_u, petname_3_u,
        cbirthdate, cbirthdate_d, cbirthdate_dd, cbirthdate_m, cbirthdate_mm, cbirthdate_y, cbirthdate_yy, cbirthdate_yyy, cbirthdate_yyyy,
    ]
    my_list.extend(a)
    c = []
    b = list(permutations(my_list, 2))
    for o in range(0, len(b)):
        if len(b[o][0]+b[o][1])>=6:
            c.append(b[o][0]+b[o][1])
    for k in my_list:
        for o in range(0, len(b)):
            if len(b[o][0]+b[o][1])>=6:
                c.append(b[o][0]+k+b[o][1])
                c.append(b[o][0]+b[o][1]+k)
                c.append(k+b[o][0]+b[o][1])
    return c


file = open(f'{first_name}''.txt', 'a')
for i in permut():
    file.write(i)
    file.write('\n')
file.close()


def repeat():
    lines = open(f'{first_name}''.txt', 'r').readlines()
    lines_set = set(lines)
    final = open(f'{first_name}''.txt', 'w')
    for line in lines_set:
        final.write(line)


repeat()