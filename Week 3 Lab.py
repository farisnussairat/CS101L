Python 3.9.11 (tags/v3.9.11:2de452f, Mar 16 2022, 14:33:45) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Welcome to the Flarsheim Guesser!")
Welcome to the Flarsheim Guesser!
>>> while(1):
    print("Please think of a number between and including 1 and 100")
    print()
    remainder_3=0
    remainder_5=0
    remainder_7=0
    while(1):
        print("What is the remainder when your number is divided by 3?")
        remainder_3=int(input())
        if(remainder_3>2):
                    print("The value entered must be less than 3")
                    continue
        elif(remainder_3<0):
            print("Value entered must be 0 or greater")
            continue
        else:
            break
    print()
    while(1):
        print("What is the remainder when your number is divided by 5? ")
        rem5=int(input())
        if(remainder_5>4):
                    print("Value entered must be less than 5")
                    continue
        elif(remainder_5<0):
            print("Value entered must be 0 or greater")
            continue
        else:
            break
    print()
    while(1):
        print("What is the remainder when your number is divided by 7?")
        remainder_7=int(input())
        if(remainder_7>6):
                    print("Value entered must be lesss than 7")
                    continue
        elif(remainder_7<0):
            print("The value entered must be 0 or graeater")
            continue
        else:
            break    
    
    i=1
    while i<=100:
        if((i%3==remainder_3)and(i%5==remainder_5)and(i%7==remainder_7)):
            break
        i=i+1
    print("Your Number was ",i)
    print("How amazing is that?")
    
    print()
    
    user_answer=0
    while(1):
        print("Do you want to play again Y to continue, N to quit  ==> ",end="")
        
        user_answer=input()
        if(user_answer=="Y" or user_answer=="y" or user_answer=="N" or user_answer=="n"):
            break
        else:
                continue
    print()
    if(user_answer=="N" or user_answer=="n"):
        break
