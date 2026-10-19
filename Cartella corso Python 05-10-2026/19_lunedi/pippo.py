


File_valorizzato_da_open= open("Cartella corso Python 05-10-2026/19_lunedi/pippo.txt","r")
print(File_valorizzato_da_open)

#metodo di lettura totale del file
contenuto_file_totale= File_valorizzato_da_open.read()
print (contenuto_file_totale)


# metodo di lettura line by line del file
contenuto_file_riga= File_valorizzato_da_open.readline()
print(contenuto_file_riga)

#metodo di chiusura del file e disimpegnare la ram
File_valorizzato_da_open.close()

#metodo si scrittura che sovrascrivera' il file gia creato
File_valorizzato_da_open= open("Cartella corso Python 05-10-2026/19_lunedi/pippo.txt","w")
File_valorizzato_da_open.write("ciao sono sempronio")
File_valorizzato_da_open.close()


#sara sempre un close
with open("Cartella corso Python 05-10-2026/19_lunedi/pippo.txt","r") as file:
    contenuto= file.read()



