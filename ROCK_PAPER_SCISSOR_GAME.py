import random
rock="""
             _______
            /____(__)_
    _______/_______(__)
            _______(__)
    _______\ _______(_)
            \______(_)  
"""

paper="""
            _________
          /    _____ )
_________/      _________)
                __________)
_________\       _______)
          \_______)
            
"""
scissor="""
          __      
         /___)________
________/   __________)
            __________)
________\     __(_)
         \___(_)        
"""
while(True):
        enter=input("if you want to play game ('yes' for play/'No' for exit)")
        if(enter=="yes"):
              

                c_r=0
                y_r=0
                n=int(input("Enter how many times do you want to play(Note:please enter odd number only)"))
                if(n%2!=0):
                        for i in range(n):
                                g_images=[rock,paper,scissor]
                                print("0-rock/1-paper/2-scissor")
                                user_input=int(input("Enter your choice"))
                                print("your choice is:\n")
                                print(g_images[user_input])
                                computer_choice=random.randint(0,2)
                                print("Computer choice is:\n")
                                print(g_images[computer_choice])
                                for i in range(1):
                                        if(user_input==computer_choice):
                                                print("Tie!No point for both")
                                        elif(computer_choice==0 and user_input==2):
                                                print("computer got 1 point!")
                                                c_r+=1
                                        elif(computer_choice==2 and user_input==0):
                                                print("you got 1 point!")
                                                y_r+=1
                                        elif(computer_choice>user_input):
                                                print("computer got 1 point!")
                                                c_r+=1
                                        elif(user_input>computer_choice):
                                                print("you got 1 point!")
                                                y_r+=1
                                        else:
                                                 print("something wrong")
                        print("***********************************************")
                        print("Final score")
                        print("___________")
                        print("computer points:",c_r)
                        print("your points:",y_r)
                        if(c_r==y_r):
                                print("you both are tie !try to play again ")
                        elif(c_r>y_r):
                                print("computer win the game")
                        elif(y_r>c_r):
                                print("you win the game")
                        elif(y_r==0 and c_r==0):
                                print("both are lose the game")
                else:
                        print("please enter odd num(1,3,5,7,9)")
        else:
                quit()        
        
