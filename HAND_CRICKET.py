import random
chance=int(input("enter number of bowl:"))
print(chance)
scoreu=0
scorec=0
l=['head','tail']
l1=['bat','bowl']
tc=random.choice(l)
tu=input("what will you choose for toss head or tail? : ")
print("you choose",tu,"........")
print("................................")
print("let's check result of toss......")

if tc==tu:
    print("you won the toss........")
    print("now you can choose batting or bowling.........")
    gu=input("what will you want to play bat or bowl? : ")
    print("you choose",gu,"........")
    if gu=='bat':
        print("now,you perform the batting...")
        for i in range(chance):
            fc=random.randint(1,10)
            fu=int(input("enter your number: "))
            if fc!=fu:
                scoreu+=fu
                print("your score:",scoreu)
            else:
                print("your final score:",scoreu)
                print("sorry...you are out.....")
                break

        print("your batting is complete......")
        print("...............................")
        print("now,it's time for bowling.......")

        for i in range(chance):
            fc=random.randint(1,10)
            fu=int(input("enter your number: "))
            if fc!=fu:
                scorec+=fc
                print("your score:",scorec)
            else:
                print("your final score:",scorec)
                print("ABHINANDAN ABHINANDAN ABHINANDAN")
                print("computer is out...")
                break
        print(".................................")
        print("let,s check the result......")
        print(".................................")
        if scoreu==scorec:
            print("game is tieeee..........")
        if scoreu<scorec:
            print("good try,but you loss the game.........")
        if scoreu>scorec:
            print("congo...,you won the game.........")
        print("game is over....")
    else:
        print("now,you perform the bowling....")
        for i in range(chance):
            fc=random.randint(1,10)
            fu=int(input("enter your number: "))
            if fc!=fu:
                scorec+=fc
                print("your score:",scorec)
            else:
                print("your final score:",scorec)
                print("ABHINANDAN ABHINANDAN ABHINANDAN")
                print("computer is out...")
                break

        
        print("your bowling is complete......")
        print("...............................")
        print("now,it's time for batting.......")

        for i in range(chance):
            fc=random.randint(1,10)
            fu=int(input("enter your number: "))
            if fc!=fu:
                scoreu+=fu
                print("your score:",scoreu)
            else:
                print("your final score:",scoreu)
                print("sorry...you are out.....")
                break
        print(".................................")
        print("let,s check the result......")
        print(".................................")
        if scoreu==scorec:
            print("game is tieeee..........")
        if scoreu<scorec:
            print("good try,but you loss the game.........")
        if scoreu>scorec:
            print("congo...,you won the game.........")
        print("game is over....")

else:
    print("computer won the toss........")
    print("now,computer will choose its choise bat or bowl.....")
    gc=random.choice(l1)
    print("computer choose",gc,"........")
    if gc=='bat':
        print("now,you perform the bowling...")
        for i in range(chance):
            fc=random.randint(1,10)
            fu=int(input("enter your number: "))
            if fc!=fu:
                scorec+=fc
                print("your score:",scorec)
            else:
                print("your final score:",scorec)
                print("ABHINANDAN ABHINANDAN ABHINANDAN")
                print("computer is out...")
                break

        print("your bowling is complete......")
        print("...............................")
        print("now,it's time for batting.......")

        for i in range(chance):
            fc=random.randint(1,10)
            fu=int(input("enter your number: "))
            if fc!=fu:
                scoreu+=fu
                print("your score:",scoreu)
            else:
                print("your final score:",scoreu)
                print("sorry...you are out.....")
                break
        print(".................................")
        print("let,s check the result......")
        print(".................................")
        if scoreu==scorec:
            print("game is tieeee..........")
        if scoreu<scorec:
            print("good try,but you loss the game.........")
        if scoreu>scorec:
            print("congo...,you won the game.........")
        print("game is over....")

    else:
        print("now,you perform the batting....")
        for i in range(chance):
            fc=random.randint(1,10)
            fu=int(input("enter your number: "))
            if fc!=fu:
                scoreu+=fu
                print("your score:",scoreu)
            else:
                print("your final score:",scoreu)
                print("sorry...you are out.....")
                break

        
        print("your batting is complete......")
        print("...............................")
        print("now,it's time for bowling.......")

        for i in range(chance):
            fc=random.randint(1,10)
            fu=int(input("enter your number: "))
            if fc!=fu:
                scorec+=fc
                print("your score:",scorec)
            else:
                print("your final score:",scorec)
                print("ABHINANDAN ABHINANDAN ABHINANDAN")
                print("computer is out...")
                break
        print(".................................")
        print("let,s check the result......")
        print(".................................")
        if scoreu==scorec:
            print("game is tieeee..........")
        if scoreu<scorec:
            print("good try,but you loss the game.........")
        if scoreu>scorec:
            print("congo...,you won the game.........")
        print("game is over....")

    


        

        
        
        

        
                
        
          
          
