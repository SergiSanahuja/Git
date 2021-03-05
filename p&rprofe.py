resposta = ""
punts = 0
preguntes_be = 0
preguntes_malament = 0
resposta = input("quin any estem? ")
if resposta == "2021":
    print ("molt bé")
    punts +=10
    preguntes_be += 1
    
else:
    punts -= 5
    print ("incorrecte")
    preguntes_malament +=1 
    
print ("respostes incorrectes: ", preguntes_malament)
print ("respostes correctes: ", preguntes_be)
print ("punts: ", punts)
    