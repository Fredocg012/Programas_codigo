import time

def busquedaLinealCentinela(A,n,x):
	tmp=A[n-1] #Se guarda el ultimo elemento de la lista en una variable temporal
	A[n-1]=x #El ultimo numero de la lista se reempleza por el numero a buscar (centinela)
	k=0
	while A[k] != x:
		k=k+1
	print("Numero de iteraciones: "+str(k+1))
	A[n-1]=tmp #Se regresa el valor que tenia la lista al final
	if k<n-1 or A[n-1]==x:
		return k #retorna el indice de la llave
	else:
		return -1 #No se encontro la llave

A=[33,25,16,38,56,1,5,9,18,96,25,14,76,32,25,17,1,4,8]
#A=[1,1,1,5,8,9,14,16,17,18,25,25,25,32,33,38,56,76,96]
tiempo_in=time.clock()
x=busquedaLinealCentinela(A,len(A),1)
print("Indice de la llave: "+str(x))
tiempo_fin=time.clock()
tiempo_tot=tiempo_fin-tiempo_in
print("Tiempo de procesamiento: "+str(tiempo_tot)+" segundos")
