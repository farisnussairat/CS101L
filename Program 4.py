Python 3.9.11 (tags/v3.9.11:2de452f, Mar 16 2022, 14:33:45) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Faris Nussairat Program 4 email:Fmnw9x@umsystem.edu
import random
import math

def play_again():
    again = str(input('Do you want to play again?, y for yes, n for no\n'))
    if again == 'y' or again == 'yes':
        return True
    elif again == 'n' or again == 'no':
        return false
    else:
        print('you must enter y/yes or n/no to continue. please try again.')
def get_wager(bank: int):
    wager = int(input('how many chips do you want to wager?\n'))
    if wager > 0 and wager <= bank:
        return wager
    elif wager > 0 and wager > bank:
        print('The wager amount cant be greater than how much you have.')
        wager = int(input('How many chips do you wat to wager?\n'))
    else:
        print('The wager must be greater than 0. Try again.')
        wager = int(input('How many chips do you want to wager?\n'))
def get_slots_results():
    random_num1 = random.randint(1, 10)
    random_num2 = random.randint(1, 10)
    random_num3 = random.randint(1, 10)
    return random_num1, random_num2, random_num3
def get_matches(reelA,reelB, reelC):
    if reelA == reelB and reelA == reelC:
        matches = 2
        return matches
    else:
        return 0
def get_bank():
    chips = int(input('How many chips do you want to start?\n'))
    if chips > 0 and chips < 101:
        return chips
    elif chips < 0:
        print('too low, omly 1-100 chips')
        chips = int(input('How many chips do you want to start?\n'))
def get_payout(wager, matches):
    if matches == 3:
        return(wager * 10) - wager
    elif matches == 2:
        return(wager * 3) - wager
    else:
        return wager 
if __name__ == '__main__':

    playing = True
    while playing:

        bank = get_bank()
        spins = 0
        bank_list = []

        while True:
            wager = get_wager(bank)

            reelA,reelB,reelC =get_slots_results()
            matches = get_matches(reelA,reelB,reelC)
            payout = get_payout(wager, matches)
            bank = str(bank) + 'payout'
            print('your spin', reelA, reelB, reelC)
            print('matched', matches, 'reels')
            print('you won/lost', payout)
            print('current bank', bank)
            print()
        print('you lost all', bank_list[0], 'in', spins, 'spins')
        print('the most chips you had was', max(bank_list))
        playing = play_again()