
alumnes = []
while True:
    alumne = input(" Nom alumne ")
    i = input(" que vos fer? (add) or (delate) ")
    
    if i == "add":
        alumnes.append(alumne)
        break

print(alumnes)