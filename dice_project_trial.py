"""
print("MINI_PROJECT")
print("Project: Dice Simulator Game With regular and Hack Version")
print("DEVELOPER_NAME:SAURABH SANTOSH AHER")
print("Batch:Python")
print("Guide by :AMOL Bhavsar Sir")
print("DATE = 24/07/2022,Sunday,1:28 PM")


"""





import random

def lets_play():
           play = 0
           while(1):
                print("1: Roll DICE\n2: STOP")
                play = int(input("Enter:>"))

                if(play == 1):
                            rolls = random.choices([1, 2, 3, 4, 5, 6], weights=[10, 10, 10, 10, 10, 10], k=1)
                            print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
                            print("YOUR DICE NUMBER=>>> ",rolls)
                            print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")

                elif(play == 2):
                           exit()
def lets_play_mod():
                 print("_____________________________WELCOME TO MOD VERSION________________________________")
                 Prob_Number=0
                 Prob_Number = int(input("TELL ME WHICH NUMBER PROBABILITY MUST BE HIGH(1,2,3,4,5,6):>"))
                 if(Prob_Number==1):
                     fun_1()
                 elif(Prob_Number==2):
                     fun_2()
                 elif (Prob_Number == 3):
                     fun_3()
                 elif (Prob_Number == 4):
                     fun_4()
                 elif (Prob_Number == 5):
                     fun_5()
                 elif (Prob_Number == 6):
                     fun_6()
                 else:
                     print("INVALID INPUT")


def fun_1():
    while(1):
          print("YOUR CODE IS 1")
          play=0
          print("1: Roll DICE\n2: Continue with CODE 1\n3: Change Probability")
          play=int(input("Enter:>"))

          if(play==1):
                     rolls = random.choices([1, 2, 3, 4, 5, 6], weights=[100, 10, 10, 10, 10, 10], k=1)
                     print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
                     print("YOUR DICE NUMBER=>>> ", rolls)
                     print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")

          elif(play==2):
                       fun_1()

          elif(play==3):
                      lets_play_mod()
          else:
               print("ENTER VALID INPUT!!!!")

def fun_2():
    while(1):
          print("YOUR CODE IS 2")
          play=0
          print("1: Roll DICE\n2: Continue with CODE 2\n3: Change Probability")
          play=int(input("Enter:>"))

          if(play==1):
                     rolls = random.choices([1, 2, 3, 4, 5, 6], weights=[10, 100, 10, 10, 10, 10], k=1)
                     print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
                     print("YOUR DICE NUMBER=>>> ", rolls)
                     print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")


          elif(play==2):
                       fun_2()

          elif(play==3):
                      lets_play_mod()
          else:
               print("ENTER VALID INPUT!!!!")

def fun_3():
    while(1):
          print("YOUR CODE IS 3")
          play=0
          print("1: Roll DICE\n2: Continue with CODE 3\n3: Change Probability")
          play=int(input("Enter:>"))

          if(play==1):
                     rolls = random.choices([1, 2, 3, 4, 5, 6], weights=[10, 10, 100, 10, 10, 10], k=1)
                     print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
                     print("YOUR DICE NUMBER=>>> ", rolls)
                     print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")


          elif(play==2):
                       fun_3()

          elif(play==3):
                      lets_play_mod()
          else:
               print("ENTER VALID INPUT!!!!")


def fun_4():
    while(1):
          print("YOUR CODE IS 4")
          play=0
          print("1: Roll DICE\n2: Continue with CODE 4\n3: Change Probability")
          play=int(input("Enter:>"))

          if(play==1):
                     rolls = random.choices([1, 2, 3, 4, 5, 6], weights=[10, 10, 10, 100, 10, 10], k=1)
                     print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
                     print("YOUR DICE NUMBER=>>> ", rolls)
                     print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")


          elif(play==2):
                       fun_4()

          elif(play==3):
                      lets_play_mod()
          else:
               print("ENTER VALID INPUT!!!!")


def fun_5():
    while(1):
          print("YOUR CODE IS 5")
          play=0
          print("1: Roll DICE\n2: Continue with CODE 5\n3:Change Probability")
          play=int(input("Enter:>"))

          if(play==1):
                     rolls = random.choices([1, 2, 3, 4, 5, 6], weights=[10, 10, 10, 10, 100, 10], k=1)
                     print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
                     print("YOUR DICE NUMBER=>>> ", rolls)
                     print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")


          elif(play==2):
                       fun_5()

          elif(play==3):
                      lets_play_mod()
          else:
               print("ENTER VALID INPUT!!!!")


def fun_6():
    while(1):
          print("YOUR CODE IS 6")
          play=0
          print("1: Roll DICE\n2: Continue with CODE 6\n3: Change Probability\n4:STOP")
          play=int(input("Enter:>"))

          if(play==1):
                     rolls = random.choices([1, 2, 3, 4, 5, 6], weights=[10, 10, 10, 10, 10, 100], k=1)
                     print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
                     print("YOUR DICE NUMBER=>>> ", rolls)
                     print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")


          elif(play==2):
                       fun_6()

          elif(play==3):
                      lets_play_mod()
          elif(play==4):
                    exit()
          else:
               print("ENTER VALID INPUT!!!!")


def display():
        print("________________________________DICE SIMULATOR GAME__________________________ ")
        print("Do you want play MOD version or Regular?")
        print("1: Mod Version")
        print("2: Default Version")
        input1 = 0
        input1 = int(input("Enter Your Input:>"))

        if(input1 == 1):
            print("You Choose MOD version")
            lets_play_mod()
        elif(input1 == 2):
            print("You Choose Default version")
            lets_play()
        else:
            print("ENTER VALID INPUT!!!")

display()




