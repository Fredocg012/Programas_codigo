def BusquedaBinIter(l,x,izquierda,derecha):
	i=0
	while izquierda<=derecha:
		i+=1
		medio = (izquierda+derecha)//2
		if l[medio]==x:
			print("Numero de iteraciones: "+str(i))
			return medio
		elif l[medio]<x:
			izquierda=medio+1
		else:
			derecha=medio-1
	print("Numero de iteraciones: "+str(i))
	return -1

l=[1,1,1,5,8,9,14,16,17,18,25,25,25,32,33,38,56,76,96]
#l=[33,25,16,38,56,1,5,9,18,96,25,14,76,32,25,17,1,4,8]
ind=BusquedaBinIter(l,1,0,len(l)-1)
print("Indice de la llave: "+str(ind))
