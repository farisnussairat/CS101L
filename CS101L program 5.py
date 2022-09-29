Python 3.9.11 (tags/v3.9.11:2de452f, Mar 16 2022, 14:33:45) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #CS101 Lab Faris Nussairat
#program number 5
#email: Fmnw9x@umsystem.edu
#Problem: The Linda Hall library wants to come up with a new library card numbering system for students.
#The card number’s first 5 characters are A-Z, which will normally be the first five characters of
#the student’s name.  The next character at index 5 is a string value either 1, 2, or 3 which
#represents the different schools; SCE, School of Law, or College of arts and Sciences.  The
#character at index 6 is either 1, 2, 3, or 4.  These are the grade levels; Freshman, Sophomore,
#Junior, and Senior.  The next 2 characters are 0-9, and the last character at index 9 is the check
#digit to verify the previous values.  The last character is also 0-9.

import string


def character_value(char: str) -> int:
    if char.isalpha():
        return string.ascii_uppercase.index(char)
    elif char.isnumeric():
        return int(char)


def get_check_digit(libarycard: str) -> int:
    check = libarycard[9]
    letters = libarycard[0:5]
    numbers = []
    for x in letters:
        a = string.ascii_uppercase.index(x)
        numbers.append(a)
    for x in libarycard[5:10]:
        numbers.append(character_value(x))
    sum = 0
    for x in range(len(numbers)):
        sum += (x + 1) * (numbers[x])
    return sum % 10


def verify_check_digit(libarycard: str) -> tuple:
    if len(libarycard) != 10:
        return (False, 'The length of the number given must be 10')
    elif llibarycard[0:5].isalpha() == False:
        for x in libarycard[0:5]:
            if x.isalpha() != True:
                index = libarycard.find(x)
                val = x
        return (False, 'The first 5 charcters must be A-Z, the invalid  charcter is at {} is {}'.format(index, val))
    elif libarycard[7:10].isnumeric() != True:
        for x in libarycard[7:10]:
            if character_value(x) not in range(0, 10) or x.isalpha():
                val = x
                num = libarycard[7:10].find(x) + 7
        return (False, 'The last 3 charcters must be 0-9, the invalid charcter is at {} is {}'.format(num, val))
    elif libarycard[5] not in ['1', '2', '3']:
        return (False, 'The sixth charcter must be 1 2 or 3')
    elif libarycard[5] not in ['1', '2', '3', '4']:
        return (False, 'The seventh charcter must be 1 2 3 or 4')
    elif int(libarycard[9]) != get_check_digit(libarycard) or libarycard[9].isalpha():
        return (
        False, 'Check digit {} does not match calculated value {}.'.format(libarycard[9], get_check_digit(libarycard)))
    else:
        return True, ''


def get_school(libarycard: str) -> str:
    num = int(libarycard[5])
    if num == 1:
        return 'school of computing and Engineering CSE'
    if num == 2:
        return 'school of Law'
    if num == 3:
        return 'College of Arts and Sciences'
    else:
        return 'Invalid School'


def get_grade(libarycard: str) -> str:
    num = int(libarycard[6])
    grade = {1: 'Freshman', 2: 'Sophmore', 3: 'Junior', 4: 'Senior', 5: 'Invalid grade'}
    return grade[num]


if __name__ == '__main__':
    print("{:^60}".format('linda Hall'))
    print("{:^60}".format('Library card check'))
    print("=" * 60)

    while True:
        print()
        card_num = input('Enter Libabry card. Hit  enter to exit').upper().strip()
        if card_num == "":
            break
        result, error = verify_check_digit(card_num)
        if result == True:
            print('Invalid Library card')
            print('The card Belongs to a {}'.format(get_grade(card_num)))
        else:
            print('Library card is invalid')
            print(error)