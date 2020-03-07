import random
import os
rand = random.randint(1,6)
quit = False
while quit == False:
    target = 0
    overs  = 30 #5-overs
    choice = int(input("Enter your Choice\npress 1 = HEAD\npress 2 = Tail\n"))
    if choice == 2:
        toss = int(input("\nFor Toss\tEnter a number between 1 to 6: "))
        if (toss+rand) % 2 ==0:
            print("\nIts Tail x...................x You Won the TOSS\n")
            op = int(input("What You Want to Chose?? \n  BAT[1]\n  BOWL[2]\n"))
            if op ==1:
                print("\nIF you entered above the range you will automatically 'out'\n".upper())
                while overs !=0:
                    rand = random.randint(1,6)
                    runs = int(input("Runs Between 1 to 6\t"))
                    if rand == runs or runs >6:
                        print("\nx..........................................x\nYou're OUT")
                        break
                    else:
                        target += runs
                        print("Computer Chose", rand)
                        print(f"Current Score is {target}")
                        overs-=1
                        print(f"Balls Left {overs}")
                os.system('clear')
                print("\nYou Given the target to Computer is = \n".upper(), target)
                overs = 30
                i= 0
                print("\nIF you entered above the range you will automatically 'out'\n".upper())
                while overs !=0:
                    rand = random.randint(1,6)
                    runs = int(input("BOWL Between 1 to 6\t"))
                    if rand == runs:
                        print("\nx..........................................x\nComputer is OUT\tYou Win")
                        break
                    else:
                        target -= rand
                        print("Computer HITS", rand)
                        i += rand 
                        print(f"Current Score is {i}")
                        overs-=1
                        print(f"Balls Left {overs}")
                        if target <0 or target == 0:
                            print("Better LUCK NEXT TIME\tYOU LOSE :) ")
                            break
            if op ==2:
                print("\nIF you entered above the range you will automatically 'out'\n".upper())
                while overs !=0:
                    rand = random.randint(1,6)
                    runs = int(input("BOWL Between 1 to 6\t"))
                    if rand == runs:
                        print("\nx..........................................x\nComputer is OUT")
                        break
                    else:
                        print("Computer HITS", rand)
                        target += rand
                        print(f"Current Score is {target}")
                        overs-=1
                        print(f"Balls Left {overs}")
                os.system('clear')
                print("\nTarget given by computer = \t".upper(), target)
                overs = 30
                i= 0
                print("\nIF you entered above the range you will automatically 'out'\n".upper())
                while overs !=0:
                    rand = random.randint(1,6)
                    runs = int(input("Runs Between 1 to 6\t"))
                    if rand == runs or runs ==0:
                        print("\nx..........................................x\nYou're OUT")
                        print("BETTER LUCK NEXT TIME")
                        break
                    else:
                        target -= runs
                        print("Computer Chose", rand)
                        i += runs
                        print(f"Current Score is {i}")
                        overs-=1
                        print(f"Balls Left {overs}")
                        if target <0 or target == 0:
                            print("\tYOU WIN Xd ")
                            break
        else:
            print("\nIts HEAD x...................x Computer Won the TOSS\n")
            if rand%2==0:
                print("/nCOMPUTER CHOSE BOWLING")
                print("\nIF you entered above the range you will automatically 'out'\n".upper())
                while overs !=0:
                    rand = random.randint(1,6)
                    runs = int(input("Runs Between 1 to 6\t"))
                    if rand == runs or runs >6:
                        print("\nx..........................................x\nYou're OUT")
                        break
                    else:
                        target += runs
                        print("Computer Chose", rand)
                        print(f"Current Score is {target}")
                        overs-=1
                        print(f"Balls Left {overs}")
                os.system('clear')
                print("\nYou Given the target to Computer is = \n".upper(), target)
                overs = 30
                i= 0
                print("\nIF you entered above the range you will automatically 'out'\n".upper())
                while overs !=0:
                    rand = random.randint(1,6)
                    runs = int(input("BOWL Between 1 to 6\t"))
                    if rand == runs:
                        print("\nx..........................................x\nComputer is OUT\tYou Win")
                        break
                    else:
                        target -= rand
                        print("Computer HITS", rand)
                        i += rand 
                        print(f"Current Score is {i}")
                        overs-=1
                        print(f"Balls Left {overs}")
                        if target <0 or target == 0:
                            print("Better LUCK NEXT TIME\tYOU LOSE :) ")
                            break
            else:
                print("/nCOMPUTER CHOSE BATING")
                print("\nIF you entered above the range you will automatically 'out'\n".upper())
                while overs !=0:
                    rand = random.randint(1,6)
                    runs = int(input("BOWL Between 1 to 6\t"))
                    if rand == runs:
                        print("\nx..........................................x\nComputer is OUT")
                        break
                    else:
                        print("Computer HITS ", rand)
                        target += rand
                        print(f"Current Score is {target}")
                        overs-=1
                os.system('clear')
                print("\nTarget given by computer = \t".upper(), target)
                overs = 30
                i= 0
                print("\nIF you entered above the range you will automatically 'out'\n".upper())
                while overs !=0:
                    rand = random.randint(1,6)
                    runs = int(input("Runs Between 1 to 6\t"))
                    if rand == runs:
                        print("\nx..........................................x\nYou're OUT")
                        break
                    else:
                        target -= runs
                        print("Computer Chose ", rand)
                        i += runs
                        print(f"Current Score is {i}")
                        overs-=1
                        print(f"Balls Left {overs}")
                        if target <0 or target == 0:
                            print("\tYOU WIN Xd ")
                            break
    elif choice == 1:
        toss = int(input("\nFor Toss\tEnter a number between 1 to 6: "))
        if (toss+rand) % 2 !=0:
            if (toss+rand+choice) % 2 ==0:
                print("\nIts HEAD x...................x You Won the TOSS\n")
            op = int(input("What You Want to Chose?? \n  BAT[1]\n  BOWL[2]\n"))
            if op ==1:
                print("\nIF you entered above the range you will automatically 'out'\n".upper())
                while overs !=0:
                    rand = random.randint(1,6)
                    runs = int(input("Runs Between 1 to 6\t"))
                    if rand == runs or runs >6:
                        print("\nx..........................................x\nYou're OUT")
                        break
                    else:
                        target += runs
                        print("Computer Chose", rand)
                        print(f"Current Score is {target}")
                        overs-=1
                        print(f"Balls Left {overs}")
                os.system('clear')
                print("\nYou Given the target to Computer is = \n".upper(), target)
                overs = 30
                i= 0
                print("\nIF you entered above the range you will automatically 'out'\n".upper())
                while overs !=0:
                    rand = random.randint(1,6)
                    runs = int(input("BOWL Between 1 to 6\t"))
                    if rand == runs:
                        print("\nx..........................................x\nComputer is OUT\tYou Win")
                        break
                    else:
                        target -= rand
                        print("Computer HITS", rand)
                        i += rand 
                        print(f"Current Score is {i}")
                        overs-=1
                        print(f"Balls Left {overs}")
                        if target <0 or target == 0:
                            print("Better LUCK NEXT TIME\tYOU LOSE :) ")
                            break
            if op ==2:
                print("\nIF you entered above the range you will automatically 'out'\n".upper())
                while overs !=0:
                    rand = random.randint(1,6)
                    runs = int(input("BOWL Between 1 to 6\t"))
                    if rand == runs:
                        print("\nx..........................................x\nComputer is OUT")
                        break
                    else:
                        print("Computer HITS", rand)
                        target += rand
                        print(f"Current Score is {target}")
                        overs-=1
                        print(f"Balls Left {overs}")
                os.system('clear')
                print("\nTarget given by Computer  = \t".upper(), target)
                overs = 30
                i= 0
                print("\nIF you entered above the range you will automatically 'out'\n".upper())
                while overs !=0:
                        rand = random.randint(1,6)
                        runs = int(input("Runs Between 1 to 6\t"))
                        if rand == runs or runs ==0:
                            print("\nx..........................................x\nYou're OUT")
                            print("BETTER LUCK NEXT TIME")
                            break
                        else:
                            target -= runs
                            print("Computer Chose", rand)
                            i += runs
                            print(f"Current Score is {i}")
                            overs-=1
                            print(f"Balls Left {overs}")
                            if target <0 or target == 0:
                                print("\tYOU WIN Xd ")
                                break
        else:
            print("\nIts TAIL x...................x Computer Won the TOSS\n")
            if rand%2!=0:
                print("/nCOMPUTER CHOSE BOWLING")
                print("\nIF you entered above the range you will automatically 'out'\n".upper())
                while overs !=0:
                    rand = random.randint(1,6)
                    runs = int(input("Runs Between 1 to 6\t"))
                    if rand == runs or runs >6:
                        print("\nx..........................................x\nYou're OUT")
                        break
                    else:
                        target += runs
                        print("Computer Chose", rand)
                        print(f"Current Score is {target}")
                        overs-=1
                        print(f"Balls Left {overs}")
                os.system('clear')
                print("\nYou Given the target to Computer is = \n".upper(), target)
                overs = 30
                i= 0
                print("\nIF you entered above the range you will automatically 'out'\n".upper())
                while overs !=0:
                    rand = random.randint(1,6)
                    runs = int(input("BOWL Between 1 to 6\t"))
                    if rand == runs:
                        print("\nx..........................................x\nComputer is OUT\tYou Win")
                        break
                    else:
                        target -= rand
                        print("Computer HITS", rand)
                        i += rand 
                        print(f"Current Score is {i}")
                        overs-=1
                        print(f"Balls Left {overs}")
                        if target <0 or target == 0:
                            print("Better LUCK NEXT TIME\tYOU LOSE :) ")
                            break
            else:
                print("/nCOMPUTER CHOSE BATING")
                print("\nIF you entered above the range you will automatically 'out'\n".upper())
                while overs !=0:
                    rand = random.randint(1,6)
                    runs = int(input("BOWL Between 1 to 6\t"))
                    if rand == runs:
                        print("\nx..........................................x\nComputer is OUT")
                        break
                    else:
                        print("Computer Chose", rand)
                        target += rand
                        print(f"Current Score is {target}")
                        overs-=1
                        print(f"Balls Left {overs}")
                os.system('clear')
                print("\nTarget given by computer = \t".upper(), target)
                overs = 30
                i= 0
                print("\nIF you entered above the range you will automatically 'out'\n".upper())
                while overs !=0:
                        rand = random.randint(1,6)
                        runs = int(input("Runs Between 1 to 6\t"))
                        if rand == runs:
                            print("\nx..........................................x\nYou're OUT")
                            break
                        else:
                            target -= runs
                            print("Computer Chose", rand)
                            i += runs
                            print(f"Current Score is {i}")
                            overs-=1
                            print(f"Balls Left {overs}")
                            if target <0 or target == 0:
                                print("\tYOU WIN Xd ")
                                break
    else:
        continue
    if quit == False:
        play = int(input("Are You Want To \n PLAY AGAIN = 1\n QUIT =2 "))
        if play ==1:
            continue
        elif play == 2:
            break
        else:
            break