numn = 0
total = 0

while True:
    nota = int(input("Quina nota te? "))
   
    if nota < 0:
      break
    numn += 1
    total += nota
    
print (numn)
mitjana = int(total/numn)
print ("{0:.1f}" .format(mitjana))
