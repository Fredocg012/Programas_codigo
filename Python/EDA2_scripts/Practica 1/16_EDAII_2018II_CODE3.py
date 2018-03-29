import time

def merge(lista1, lista2): #Funcion encargada de mezclar las partes o divisiones de la lista A
	i=0
	j=0
	resultado = [] #lista vacia donde se guardara la mezcla entre lista 1 y lista2
	while(i < len(lista1) and j < len(lista2)):
		if (lista1[i] < lista2[j]): #Condicion encargada de ordenar de forma ascendente o descendente
			resultado.append(lista1[i])
			i=i+1
		else:
			resultado.append(lista2[j])
			j=j+1
	resultado = resultado + lista1[i:] #Mezcla
	resultado = resultado + lista2[j:]
	print(resultado) 
	return resultado

def MergeSort(A):
	print(A)
	if len(A) < 2:
		return A
	q = len(A)//2 #Linea equivalente a q=(p+r)//2
	izq = MergeSort(A[:q]) #Division de la lista A, parte izquierda y derecha
	der = MergeSort(A[q:])
	return merge(izq, der)

A=[33,25,16,38,56,1,5,9,18,96,25,14,76,32,25,17,1,4,8]
tiemp_in=time.clock()
MergeSort(A)
tiemp_fin=time.clock()
tiemp_tot=tiemp_fin-tiemp_in
print("\nTiempo de ejecucion: "+str(tiemp_tot)+" segundos\n")
