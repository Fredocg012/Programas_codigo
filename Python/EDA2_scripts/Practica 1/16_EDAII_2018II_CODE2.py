import time

def bubbleSort2(A):
	bandera=True
	pasada=0
	while pasada<len(A)-1 and bandera:
		bandera=False #Se cambia a falso, si no se hace ningun cambio dara por hecho que esta ordenado
		for j in range(len(A)-1): #Numero de comparaciones
			if(A[j]>A[j+1]):
				bandera=True #Si hace por lo menos un cambio o permutacion, el valor cambia a true
				temp=A[j]
				A[j]=A[j+1]
				A[j+1]=temp
		pasada=pasada+1
	print("\nNumero de pasadas: "+str(pasada)+"\n")

A=[33,25,16,38,56,1,5,9,18,96,25,14,76,32,25,17,1,4,8]
tiemp_in=time.clock()
bubbleSort2(A)
print(A)
tiemp_fin=time.clock()
tiemp_tot=tiemp_fin-tiemp_in
print("\nTiempo de ejecucion: "+str(tiemp_tot)+" segundos\n")
