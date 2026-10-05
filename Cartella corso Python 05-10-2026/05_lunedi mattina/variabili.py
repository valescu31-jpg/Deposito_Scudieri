#funzionalita delle variabili

nome_varabile = "valore"
numero = 1

#stringhe
v= "valerio"
print (v[1])
print (v[4])

#stringhe con integrazione del +

arrivederci = "addio"
nome= "Pasquale"
messaggio = arrivederci + " " + nome
print(messaggio)

#metodi delle stringhe 

s= "Ciao, mondo"
print(len(s)) #
print(s.upper())# out : CIAO, MONDO
print (s.split(",")) #out : "ciao", "mondo"
print (s.replace("mondo" , "universo"))#out: "Ciao, universo!"


#booleani

x=15
y=12

print (x==y) #false
print (x != y) #true
print (x < y) # false

# operatori di confronto and, or e not

x=5
y=10
z=7
print (x<y and y>z) # true 
print (x<y or z>y) # true 
print (not(x<y)) # false
