from itertools import permutations

first_name = 'emmitt'
first_name_c = first_name.capitalize()
first_name_3 = first_name[:3]
first_name_3_c = first_name_3 .capitalize()    

second_name = 'romano'
second_name_3 = second_name[:3]
second_name_c = second_name.capitalize()
second_name_3_c = second_name_3.capitalize()

surname = 'howard'
surname_3 = surname[:3]
surname_c = surname.capitalize()
surname_3_c = surname_3.capitalize()

birthdate = '15081947'
birthdate_d = birthdate[:1]
birthdate_dd = birthdate[:2]
birthdate_m = birthdate[3:4]
birthdate_mm = birthdate[2:4]
birthdate_y = birthdate[4:6]
birthdate_yy = birthdate[-2:]
birthdate_yyy = birthdate[-3:]
birthdate_yyyy = birthdate[-4:]

pfirst_name = 'melissa'
pfirst_name_3 = pfirst_name[:3]
pfirst_name_c = pfirst_name.capitalize()
pfirst_name_3_c = pfirst_name_3.capitalize()

psecond_name = 'hoggan'
psecond_name_3 = psecond_name[:3]
psecond_name_c = psecond_name.capitalize()
psecond_name_3_c = psecond_name_3.capitalize() 

pnickname = 'davis'
pnickname_3 = pnickname[:3]
pnickname_c = pnickname.capitalize()
pnickname_3_c = pnickname_3.capitalize()

pbirthdate = '01051959'
pbirthdate_d = pbirthdate[:1]
pbirthdate_dd = pbirthdate[:2]
pbirthdate_m = pbirthdate[3:4]
pbirthdate_mm = pbirthdate[2:4]
pbirthdate_y = pbirthdate[4:6]
pbirthdate_yy = pbirthdate[-2:]
pbirthdate_yyy = pbirthdate[-3:]
pbirthdate_yyyy = pbirthdate[-4:]

petname = 'baibre'
petname_3 = petname[:3]
petname_c = petname.capitalize()
petname_3_c = petname_3.capitalize()

special_text = 'flowers,fish,goat'
special_word = special_text.split(',')

snum = '1,22,123'
special_num = snum.split(',')


def permut():
    a=[first_name,first_name_c,first_name_3,first_name_3_c,
       second_name,second_name_3,second_name_c,second_name_3_c,
       surname,surname_3,surname_c,surname_3_c,
       birthdate,birthdate_d,birthdate_dd,birthdate_m,birthdate_mm,birthdate_y,birthdate_yy,birthdate_yyy,birthdate_yyyy,
       pfirst_name,pfirst_name_c,pfirst_name_3,pfirst_name_3_c,
       psecond_name,psecond_name_3,psecond_name_c,psecond_name_3_c,
       pnickname,pnickname_3,pnickname_c,pnickname_3_c,
       pbirthdate,pbirthdate_d,pbirthdate_dd,pbirthdate_m,pbirthdate_mm,pbirthdate_y,pbirthdate_yy,pbirthdate_yyy,pbirthdate_yyyy,
       petname,petname_3,petname_c,petname_3_c
       ]
    c=[]
    for i in special_word:
        a.append(i)
    for x in special_num:
        a.append(x)
    b=list(permutations(a,2))
    for o in range(0,len(b)):
        if len(b[o][0]+b[o][1])>=6: 
            c.append(b[o][0]+b[o][1])
    return c
file = open(f'{first_name}''.txt','a')
for i in permut():
    print([f'{first_name}''.txt'], i)
    file.write(i)
    file.write('\n')
file.close()