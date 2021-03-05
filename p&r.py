punt= 0 
pregunta1 = input("Qui és el rei de la selva? ")
if pregunta1 == "lleo":
    print ("correcte") 
    punt += 1
else:
    print ("incorrecte")
    punt -=1
    
pregunta2 = int(input("Suma 2+2? "))
if pregunta2 == "4":
    print ("correcte") 
    punt += 1
else:
    print ("incorrecte")
    punt -=1
    
pregunta3 = int(input("multiplica 9*9? "))
if pregunta3 == "81":
    print ("correcte") 
    punt += 1
else:
    print ("incorrecte")
    punt -=1   

pregunta4 = (input("Com es diu el profe de SOX "))
if pregunta4 == "Pere":
    print ("correcte") 
    punt += 1
else:
    print ("incorrecte")
    punt -=1

pregunta5 = int(input("Resta 20-12 "))
if pregunta5 == "8":
    print ("correcte") 
    punt += 1
else:
    print ("incorrecte")
    punt -=1    

if punt <0:
   punt =0
print(punt)