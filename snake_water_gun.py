import random 
''' 1 = snake , -1 = water , 0 = gun'''

computer = random.choice([1,-1,0])
youstr = input("Enter Your Choice:")
youdict = { "s" : 1 , "w" : -1 , "g" : 0 }
reverseDict = { 1 : "snake" , -1 : "water" , 0 : "gun"}
you = youdict[youstr]

print(f"you chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("its draw")
else:
    if(computer == 1 and you == -1):
        print("You loose!")
    elif(computer == -1 and you == 1):
        print("You Win!")
    elif(computer == 0 and you ==1):
        print("You loose!")
    elif(computer == -1 and you == 0):
            print("You loose!")
    elif(computer == 0 and you == -1):
        print("You Win!")
    elif(computer == 1 and you == 0):
        print("You Win!")
    else:
         print("Something Went Wrong")
  