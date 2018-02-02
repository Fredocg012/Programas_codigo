import random

def inserccion(list_):
	for i in xrange(len(list_)):
		temp= list_[i]
		j=i-1
		while list_[j] > temp and j>=0:
			list_[j+1]= list_[j]
			j-=1
			list_[j+1]=temp

def partir(list_,izq,der):
	piv=list_[izq]
	i,j=izq+1,der
	while True:
		while i<=j and list_[i]<=piv:
			i+=1
		while j>=i and list_[j]>=piv:
			j-=1
		if j<=i:
			break
		list_[i],list_[j]=list_[j],list_[i]
	list_[izq],list_[j]=list_[j],list_[izq]
	return j

def quickS(list_,izq,der):
	if der <= izq:
		return
	else:
		piv=partir(list_,izq,der)
		quickS(list_,izq,piv-1)
		quickS(list_,piv+1,der)

l=random.sample(range(30),10)
print 'Antes de ordenar (quickshort) ',l
quickS(l,0,len(l)-1)
print 'Ordenada',l

l=random.sample(range(30),10)
print '\n\nAntes de ordenar (inserccion) ',l
inserccion(l)
print 'Ordenada',l
