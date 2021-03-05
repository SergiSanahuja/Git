import random
num1 = random.randrange(1, 10)
num2 = random.randrange(1, 10)
op = random.randrange(0, 3)
if op == 0:
     print(num1, "+", num2)
     r = (num1 + num2)
elif op == 1:
     print(num1, "-", num2)
     r = (num1 - num2)
elif op == 2:
     print(num1, "*" ,num2)
     r = (num1 * num2)
else:
     print(num,  "/",  num2)
     r = (num1 / num2)
resposta = int(input("quin es el resultat? "))
if resposta == r:
     print("correcte")
else:
    print("incorrecte")