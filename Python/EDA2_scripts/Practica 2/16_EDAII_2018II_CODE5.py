import time

def hIzq(i):
	return 2*i

def hDer(i):
	return 2*i+1

def intercambia(A,x,y):
	tmp=A[x]
	A[x]=A[y]
	A[y]=tmp

def MinHeapify(A,i,tamanoHeap):
	L=hIzq(i)
	R=hDer(i)
	if (L<tamanoHeap and A[L]>A[i]):
		posMax=L
	else:
		posMax=i
	if (R<tamanoHeap and A[R]>A[posMax]):
		posMax=R
	if (posMax != i):
		intercambia(A,i,posMax)
		MinHeapify(A,posMax,tamanoHeap)

def construirHeapMaxIni(A,tamanoHeap):
	for i in range(len(A),-1,-1):
		MinHeapify(A,i,tamanoHeap)

def OrdenacioHeapSort(A,tamanoHeap):
	construirHeapMaxIni(A,tamanoHeap)
	for i in range(len(A)-1,0,-1):
		intercambia(A,0,i)
		tamanoHeap=tamanoHeap-1
		MinHeapify(A,0,tamanoHeap)

A=[54,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20,26,93,17,77,31,44,55,20]
tiempo_in = time.clock()
OrdenacioHeapSort(A,len(A))
print(A)
tiempo_fin = time.clock()
tiempo_tot = tiempo_fin-tiempo_in
print("\nTiempo de ejecucion: "+str(tiempo_tot)+" segundos\n")
