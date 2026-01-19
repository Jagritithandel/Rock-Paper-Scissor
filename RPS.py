import random
print("=====WELCOME IN GAME=====")
print("=====ROCK====\n====PAPER====\n====SCISSOR====\n")
userch=input("enter you choice : ").lower()
print("wow you choose : ",userch)
choices=["rock","paper","scissor"]
compch=random.choice(choices)
print("computer choose : ", compch)
if userch==compch:
    print("DRAW")
elif (userch=="rock"and compch=="scissor")or(userch=="paper"and compch=="rock")or(userch=="scissor"and compch=="paper"):
     print("===YOU WON===")
elif userch in["rock"or"paper"or"scissor"]:
     print("you lose")
else:
     print("please chosse in option\n 1. rock\n 2. paper\n 3. scissor\n")
     
    