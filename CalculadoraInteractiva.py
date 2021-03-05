

while True:
    num1 = int(input("Posa el primer num "))
    num2 = int(input("posa el segon numero "))
    operacio = input("Que vols fer [+, -, * , /, %] ")
    if operacio == "+":
        print (num1 + num2)
    elif operacio == "-":
        print (num1 - num2)
    elif operacio =="*":
        print(num1 * num2)
    elif operacio == "/":
        print(num1 / num2)
    elif operacio == "%":
        print(num1 % num2)
    elif operacio == "$":
        break
    else:
        print ("no es pot fer")