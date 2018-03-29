def busquedaLineal(A,n,x):
	encontrado=-1 #Si no se encuentra la llave en la lista retorna -1
	for k in range(n):
		if A[k] == x:
			encontrado=k #llave encontrada (indice)
	print("Numero de iteraciones: "+str(k+1)) #k+1 ya que k empieza en 0
	return encontrado #retorna el indice de la llave


A=[33,25,16,38,56,1,5,9,18,96,25,14,76,32,25,17,1,4,8]
ind=busquedaLineal(A,len(A),1)
print("Indice de la llave: "+str(ind))
