def hash(llave,m):
	suma=0
	for i in range(len(llave)):
		suma=suma+ord(llave[i])
	print("Suma: ",suma)
	return suma%m

#llave=[74+69+83+85+83+57]=[451]
print("Resultado: ",hash("JESUS9",len("JESUS9")))
#451%6=1