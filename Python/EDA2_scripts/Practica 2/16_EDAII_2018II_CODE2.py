def intercambia(A,i,j):
	temp=A[i]
	A[i]=A[j]
	A[j]=temp

def Particionar(A,p,r): #funcion encargada de particionar la lista (num_menores<=pivote<num_mayores)
	x=A[r] #toma al ultimo elemento de la lista como pivote
	i=p-1
	for j in range(p,r): #se trabaja con la lista desde su primer valor hasta el ultimo, menos uno
		if (A[j]>=x): #Condicion para que el ordenamiento sea descendente
			i=i+1
			intercambia(A,i,j)
	intercambia(A,i+1,r) #cambia de posicion al pivote
	return i+1 #nueva posicion del pivote

def QuickSort(A,p,r):
	if (p<r):
		q=Particionar(A,p,r) #posicion donde se encuentra el pivote al haber particionado
		QuickSort(A,p,q-1) #Ordena la lista con numeros menores o iguales al pivote
		QuickSort(A,q+1,r) #Ordena la lista con numeros mayores al pivote

A=[33,25,16,38,56,1,5,9,18,96,25,14,76,32,25,17,1,4,8]
QuickSort(A,0,len(A)-1)
print(A)
