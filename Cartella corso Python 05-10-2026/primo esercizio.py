
#valorizazzione delle variabili con i tipi giusti
strg = input ("inserisci una stringa")
intn =  int(input("inserisci un int"))
float = float(input("inserisci un numero reale"))
bool =  bool(input("inserisci un valore booleano (true/false):"))
char=  input("inserisci una lettera<")

#stampa variabili
print (bool, " ", float, " ", intn, " ", strg, " ", char )


#inserimento due dati numeri (interi) ceh compariamo tra di loro

numint1= int(input("inserisci un int"))
numint2= int(input("inserisci un int"))

 # comparazione operatori logici
print (numint1 < numint2 and numint1> numint2)
print (numint1< numint2 or numint1> numint2)
print (not(numint1 < numint2 and numint1> numint2))