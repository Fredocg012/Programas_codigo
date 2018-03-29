import time

def bubbleSort(A):
	for i in range(1,len(A)): #controla el numero de pasadas (n-1)
		for j in range(len(A)-1): #controla el numero de comparaciones (n-1)-1
			if A[j]>A[j+1]:
				temp=A[j]
				A[j]=A[j+1]
				A[j+1]=temp
	print("\nNumero de pasadas: "+str(i)+"\n")

A=[33,25,16,38,56,1,5,9,18,96,25,14,76,32,25,17,1,4,8]
tiemp_in=time.clock()
bubbleSort(A)
print(A)
tiemp_fin=time.clock()
tiemp_tot=tiemp_fin-tiemp_in
print("\nTiempo de ejecucion: "+str(tiemp_tot)+" segundos\n")
