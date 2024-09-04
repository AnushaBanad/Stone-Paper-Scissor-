import random
list=["stone","paper","scissor"]
cpu_score=0 
user_score=0 
i=1
n=int(input("Enter number of times you want to play:\n"))
while i<=n:
    cpu_choice=random.choice(list)
    user_choice=input("Please choose from - stone-paper-scissor\n")
    if cpu_choice==user_choice:
        print("IT'S A TIE")
    elif cpu_choice=='stone' and user_choice=='paper':
        print("YOU WON!!!\n")
        user_score=user_score+1
    elif cpu_choice=='stone' and user_choice=='scissor':
        print("CPU WON!!!\n")
        cpu_score=cpu_score+1 
    elif cpu_choice=='paper' and user_choice=='stone':
        print("CPU WON!!!\n")
        cpu_score=cpu_score+1 
    elif cpu_choice=='paper' and user_choice=='scissor':
        print("YOU WON!!!\n")
        user_score=user_score+1
    elif cpu_choice=='scissor' and user_choice=='stone':
        print("YOU WON!!!\n")
        user_score=user_score+1 
    elif cpu_choice=='scissor' and user_choice=='paper':
        print("CPU WON!!!\n")
        cpu_score=cpu_score+1
    else:
        print("YOU HAVE CHOOSEN WRONG INPUT")
    i=i+1
print("user_score=",user_score)
print("cpu_score=",cpu_score)
if cpu_score>user_score:
    print("CPU WON!!!")
elif cpu_score==user_score:
    print("IT'S A TIE")
else:
    print("YOU WON!!!")