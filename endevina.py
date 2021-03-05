import random
num1 = random.randrange(1, 100)
intents = 1 
while True:
    num2 = int(input("quin num es?" ))
    
    if num1 < num2:
        print ("es mes petit")
    elif num1 > num2:
        print ("es mes gran")
    else:
        print ("correcte")
        break
    intents +=1
    if intents == 10:
        print ("no has endevinat el número")
        break

print(intents, "intents")